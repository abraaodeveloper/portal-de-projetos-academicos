from django.shortcuts import render, redirect
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
    #print(users[0].created_at)

    return render(request, 'guest/index.html', {'posts': result[:3:1], 'users': users.count(), 'qtdAcess': 3})

def projects(request, type_content):
    softs = Soft.objects.filter(type_content=type_content)
    return render(request, 'guest/projects-list.html', {'softs': softs})

def project(request, project_slug):
    try: 
        soft = Soft.objects.get(slug=project_slug)
        soft.views = soft.views + 1
        soft.save()
        return render(request, 'guest/project.html', {'post': soft})
    except:
        print()

    try: 
        ebook = Ebook.objects.get(slug=project_slug)
        ebook.views = ebook.views + 1
        ebook.save()
        return render(request, 'guest/project.html', {'post': ebook})
    except:
        print()

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
            mainfile = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(mainfile)

            uploaded_file = request.FILES['cover']
            fs = FileSystemStorage()
            cover = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(cover)

            form.instance.file_name = mainfile
            form.instance.cover = cover

            form.instance.file_name = name
            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()

            return render(request, 'logged/dashboard.html', {'softs': softs})

    return render(request, 'logged/post-edit.html', {'softs': softs, 'form':form})

@login_required
def createEbook(request):
    form = EbookForm(request.POST or None)
    user = request.user
    softs = user.soft_set.all()

    context = {}
    if request.method == 'POST':
        if form.is_valid():

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            mainfile = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(mainfile)

            uploaded_file = request.FILES['cover']
            fs = FileSystemStorage()
            cover = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(cover)

            form.instance.file_name = mainfile
            form.instance.cover = cover

            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()

            return render(request, 'logged/dashboard.html', {'softs': softs})

    return render(request, 'logged/post-edit.html', {'softs': softs, 'form':form})

def updateEbook(request, ebook_id):
    try:
        ebook_sel = Ebook.objects.get(id = ebook_id)
    except Ebook.DoesNotExist:
        return redirect('/')
    ebook_form = EbookForm(request.POST or None, instance = ebook_sel)
    if ebook_form.is_valid():
       ebook_form.save()
       return redirect('dashboard')
    return render(request, 'logged/post-edit.html', {'form':ebook_form})

def updateSoft(request, soft_id):
    try:
        soft_sel = Soft.objects.get(id = soft_id)
    except Soft.DoesNotExist:
        return redirect('/')
    soft_form = SoftForm(request.POST or None, instance = soft_sel)
    if soft_form.is_valid():
       soft_form.save()
       return redirect('dashboard')
    return render(request, 'logged/post-edit.html', {'form':soft_form})

def deleteEbook(request, ebook_id):
    try:
        ebook_sel = Ebook.objects.get(id = ebook_id)
    except Ebook().DoesNotExist:
        return redirect('dashboard')
    ebook_sel.delete()
    return redirect('dashboard')

def deleteSoft(request, soft_id):
    try:
        soft_sel = Soft.objects.get(id = soft_id)
    except Soft().DoesNotExist:
        return redirect('dashboard')
    soft_sel.delete()
    return redirect('dashboard')