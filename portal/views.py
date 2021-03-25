from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'guest/index.html', {'posts': posts})

def project(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'guest/project.html', {'post': post})

