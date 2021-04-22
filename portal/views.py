from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.all()
    users = User.objects.all(); 
    return render(request, 'guest/index.html', {'posts': posts, 'users': users.count()})

def project(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'guest/project.html', {'post': post})

