from django.shortcuts import render, redirect

from .models import Post, Entry
from .forms import PostForm, EntryForm
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


def new_entry(request, post_id):
    """Add a new entry for a particular post."""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = post
            new_entry.save()
            return redirect('blog_app:post', post_id=post_id)

    # Display a blank or invalid form.
    context = {'post': post, 'form': form}
    return render(request, 'blog_app/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    blog = entry.blog

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:post', post_id=blog.id)

    context = {'entry': entry, 'blog': blog, 'form': form}
    return render(request, 'blog_app/edit_entry.html', context)
