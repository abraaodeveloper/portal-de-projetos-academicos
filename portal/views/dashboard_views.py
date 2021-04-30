from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from ..forms import *
from ..models import Soft, Ebook

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
    return render(request, 'guest/index.html', {'posts': result[:3:1], 'users': users.count(), 'qtdAcess': 3})

def projects(request, type_content):
    if (type_content == "software"):
        soft = Soft.objects.get(slug=project_slug)
        soft.views = soft.views + 1
        soft.save()
        return render(request, 'guest/project.html', {'post': soft})
    else:
        ebook = Ebook.objects.get(slug=project_slug)
        ebook.views = ebook.views + 1
        ebook.save()
        return render(request, 'guest/project.html', {'post': ebook})
    return redirect('home')

def project(request, project_slug):
    try: 
        soft = Soft.objects.get(slug=project_slug)
        soft.views = soft.views + 1
        soft.save()
        return render(request, 'guest/project.html', {'post': soft})
    except:
        return redirect('home')

    try: 
        ebook = Ebook.objects.get(slug=project_slug)
        ebook.views = ebook.views + 1
        ebook.save()
        return render(request, 'guest/project.html', {'post': ebook})
    except:
        return redirect('home')

# crud post
@login_required
def dashboard(request):
    user = request.user
    softs = user.soft_set.all().order_by('-views')[:3:1]
    ebooks = user.ebook_set.all().order_by('-views')[:3:1]
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
    return render(request, 'logged/dashboard.html', {'posts': result})