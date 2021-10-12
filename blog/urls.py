from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView, name='post_list'),
    path('comments/', views.CommentListView, name='com_list'),
    # path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    # path('create_post/', views.PostCreate.as_view(), name='post_create'),
    # path('user/<int:pk>/', views.user_detail, name='user_detail'),
]
