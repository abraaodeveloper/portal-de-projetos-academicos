from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import Soft, Ebook

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    softs = Soft.objects.all().order_by('-views')[:3:1]
    ebooks = Ebook.objects.all().order_by('-views')[:3:1]

    result = softs + ebooks

    if(not(len(result) < 3)):
        cont = 0
        ordenado = False
        while(cont < len(result)-1 and not(ordenado)):
            ordenado = True
            if(result[cont].views < result[cont+1].views):
                ordenado = False
                key = result[cont]
                result[cont] = result[cont+1]
                result[cont+1] = key
            cont +=1

    users = User.objects.all()

    return render(request, 'guest/index.html', {'posts': result[:3:1], 'users': users.count()})

def projects(request, type_content):
    softs = Soft.objects.filter(type_content=type_content)
    return render(request, 'guest/projects-list.html', {'softs': softs})

def project(request, project_slug):
    soft = Soft.objects.get(slug=soft_slug)
    ebook = Ebook.objects.get(slug=soft_slug)
    print(soft)
    print(ebook)
    soft.views = soft.views + 1
    soft.save()
    return render(request, 'guest/project.html', {'soft': soft})

# crud post
@login_required
def dashboard(request):
    user = request.user
    softs = user.soft_set.all()
    return render(request, 'logged/dashboard.html', {'softs': softs})

@login_required
def createSoft(request):
    form = SoftForm(request.POST or None)
    user = request.user
    softs = user.soft_set.all()

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

            return render(request, 'logged/dashboard.html', {'softs': softs})

    return render(request, 'logged/post-edit.html', {'softs': softs, 'form':form})