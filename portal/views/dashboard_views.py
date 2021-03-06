from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from ..forms import *
from ..models import Soft, Ebook

from django.contrib.auth.decorators import login_required

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