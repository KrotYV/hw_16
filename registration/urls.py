from django.urls import include, path

from registration.views import RegisterFormView, UserEditView, UserView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterFormView.as_view(), name="register"),
    path('profile/<int:pk>/', UserView.as_view(), name="profile"),
    path('profile/edit/<int:pk>/', UserEditView.as_view(), name='profile_edit'),
]
