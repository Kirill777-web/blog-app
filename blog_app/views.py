from django.shortcuts import render

from .models import Post
# Create your views here.

# The function index is the view for the home page of the blog_app.


def index(request):
    """The home page for blog_app."""
    return render(request, 'blog_app/index.html')

# One parameter is needed in the posts function, request.


def posts(request):
    """Show all topics."""
    # Query the database for all posts, sorted by date_added.
    posts = Post.objects.order_by('date_added')
    # Assign the query results to a dictionary.
    context = {'posts': posts}
    return render(request, 'blog_app/posts.html', context)
