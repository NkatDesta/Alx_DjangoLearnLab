from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, register_view, profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
]
