# api/urls.py

from django.urls import path
from .views import (
    UserCreateView, UserListView, UserDetailView,UserLoginView,
    PostCreateView, PostListView, PostDetailView,
    ProfileCreateView, ProfileListView, ProfileUpdateView, ProfileDeleteView,
    FollowUserView, UnfollowUserView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('user/login/', UserLoginView.as_view(), name='user-login'),


    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),

    path('user/follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('user/unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
