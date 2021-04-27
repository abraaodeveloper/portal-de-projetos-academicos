from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import Post

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-views')[:3:1]
    #menor = posts[0]
    '''
    for post in posts:
        if post.views < menor.views:
            menor = post
    print(menor.views)
    '''
    users = User.objects.all() 
    return render(request, 'guest/index.html', {'posts': posts, 'users': users.count()})

def projects(request, type_content):
    post = Post.objects.filter(type_content=type_content)
    return render(request, 'guest/projects-list.html', {'posts': post})

def project(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    post.views = post.views + 1
    post.save()
    return render(request, 'guest/project.html', {'post': post})

# crud post
@login_required
def dashboard(request):
    user = request.user
    posts = user.post_set.all()
    return render(request, 'logged/dashboard.html', {'posts': posts})

@login_required
def createPost(request):
    form = PostForm(request.POST or None)
    user = request.user
    posts = user.post_set.all()

    context = {}
    if request.method == 'POST':
        if form.is_valid():
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)

            form.instance.file_name = name
            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()
    '''
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()
            return render(request, 'logged/dashboard.html', {'posts': posts})
    '''
    return render(request, 'logged/post-edit.html', {'posts': posts, 'form':form})