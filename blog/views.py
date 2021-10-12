from django.shortcuts import render
from django.views import generic

from .models import Comment, Post


def index(request):
    num_posts = Post.objects.all().count()
    num_comments = Comment.objects.all().count()
    return render(request, 'blog/index.html', context={'num_posts': num_posts,
                                                       'num_comments': num_comments})


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'


class CommentListView(generic.ListView):
    model = Post
    template_name = 'blog/comment_list.html'
