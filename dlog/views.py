from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.filter(is_active=True, is_banner=True).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'dlog/index.html', context)

def details(request, slug):
    post = get_object_or_404(Post, slug=slug, is_active=True)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'dlog/details.html', context)