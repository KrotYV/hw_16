from blog.forms import RegisterForm
from blog.models import Post

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    template_name = 'registration/update_user.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'registration/user.html'


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk, is_staff=False)
    posts = Post.objects.filter(author=user).filter(posted=True)
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'obj': user,
    }
    return render(request, 'registration/user_detail.html', context)
