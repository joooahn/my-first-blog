from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('priority')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.due_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            posts = Post.objects.order_by('priority')
            return render(request, 'blog/post_list.html', {'posts' : posts})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_completed(request, pk):
    post = get_object_or_404(Post, pk=pk)
    instance = Post.objects.get(pk = pk)
    if instance.completed == False:
        instance.completed = True
    else:
        instance.completed = False
    instance.save()
    posts = Post.objects.order_by('priority')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            posts = Post.objects.order_by('priority')
            return render(request, 'blog/post_list.html', {'posts' : posts})
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    instance = Post.objects.get(pk = pk)
    instance.delete()
    posts = Post.objects.order_by('priority')
    return render(request, 'blog/post_list.html', {'posts' : posts})
