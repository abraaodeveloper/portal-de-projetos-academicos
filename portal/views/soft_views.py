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

    if request.method == 'POST':
        form = SoftForm(request.POST, request.FILES)
        if form.is_valid():

            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()

            return redirect('dashboard')
    return render(request, 'logged/post-edit.html', {'form':form})

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