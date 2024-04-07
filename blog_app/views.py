from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm
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


def post(request, post_id):
    """Show a single post and all its entries."""
    post = Post.objects.get(id=post_id)
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blog_app/post.html', context)


def new_post(request):
    """Add new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form. is_valid():
            form.save()
            return redirect('blog_app:posts')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blog_app/new_post.html', context)
