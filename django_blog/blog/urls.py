from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, register_view, profile_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
    path('post/', PostListView.as_view(), name='post_create'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]





