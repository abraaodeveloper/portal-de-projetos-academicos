from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from ..forms import *
from ..models import Soft

from django.contrib.auth.decorators import login_required

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

@login_required
def deleteSoft(request, soft_id):
    try:
        soft_sel = Soft.objects.get(id = soft_id)
    except Soft().DoesNotExist:
        return redirect('dashboard')
    soft_sel.delete()
    return redirect('dashboard')