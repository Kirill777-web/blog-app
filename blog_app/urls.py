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
    path('post/<int:post_id>/', views.post, name='post'),
    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),
    # Page to add new entry
    path('new_entry/<int:post_id>/', views.new_entry, name='new_entry'),
    # Page to edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
