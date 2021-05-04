from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from ..forms import *
from ..models import Ebook

from django.contrib.auth.decorators import login_required

@login_required
def createEbook(request):
    form = EbookForm(request.POST or None)
    user = request.user

    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.viwes = 0
            form.save()

            return redirect('dashboard')
    return render(request, 'logged/post-edit.html', {'form':form})

@login_required
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

@login_required
def deleteEbook(request, ebook_id):
    try:
        ebook_sel = Ebook.objects.get(id = ebook_id)
    except Ebook().DoesNotExist:
        return redirect('dashboard')
    ebook_sel.delete()
    return redirect('dashboard')
