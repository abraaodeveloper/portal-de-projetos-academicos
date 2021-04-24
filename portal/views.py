from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-views')[:3:1]
    users = User.objects.all() 
    return render(request, 'guest/index.html', {'posts': posts, 'users': users.count()})

def project(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    post.views = post.views + 1
    post.save()
    return render(request, 'guest/project.html', {'post': post})
