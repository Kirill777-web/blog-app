"""Define URL patterns for blog_app."""

from django.urls import path

from . import views

app_name = 'blog_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to show all posts
    path('posts/', views.posts, name='posts'),
    # Page for a single post
    path('posts/<int:post_id>/', views.post, name='post'),
    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post')

]
