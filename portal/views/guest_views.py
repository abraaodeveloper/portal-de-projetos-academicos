from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse

from ..forms import *
from ..models import Soft, Ebook

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    qtdProjetcSoft = Soft.objects.all()
    qtdProjetcEbook = Ebook.objects.all()
    qtdAcess = 0

    for s in qtdProjetcSoft:
        qtdAcess += s.views

    for e in qtdProjetcEbook:
        qtdAcess += e.views

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

    return render(request, 'guest/index.html', {
        'posts': result[:3:1],
        'users': users.count(), 
        'qtdacess': qtdAcess,
        'qtdProjetcSoft': qtdProjetcSoft.count(),
        'qtdProjetcEbook': qtdProjetcEbook.count()
    })

def getStatiscs(request):
    qtdProjetcSoft = Soft.objects.all()
    qtdProjetcEbook = Ebook.objects.all()

    datesForCreatedContent = []

    labels = []
    values = []

    for s in qtdProjetcSoft:
        datesForCreatedContent.append([str(s.created_at), 1])
    
    for s in qtdProjetcEbook:
        datesForCreatedContent.append([str(s.created_at), 1])

    for date in datesForCreatedContent:
        labels.append(date[0])
        values.append(date[1])
        #print(date[0] +"  ------   "+str(date[1]))

    return JsonResponse({"labels": labels, "values": values })

def projects(request, type_content):
    if (type_content == "software"):
        soft = Soft.objects.all()
        return render(request, 'guest/projects-list.html', {'posts': soft})
    else:
        ebook = Ebook.objects.all()
        return render(request, 'guest/projects-list.html', {'posts': ebook})
    return redirect('home')

def project(request, project_slug):
    form = CommentForm()
    try: 
        soft = Soft.objects.get(slug=project_slug)
        soft.views = soft.views + 1
        soft.save()
        comments = soft.comment_set.all()
        return render(request, 'guest/project.html', {'post': soft, 'form': form, 'comments': comments})
    except:
        print()

    try: 
        ebook = Ebook.objects.get(slug=project_slug)
        ebook.views = ebook.views + 1
        ebook.save()
        comments = ebook.comment_set.all()
        return render(request, 'guest/project.html', {'post': ebook, 'form': form, 'comments': comments})
    except:
        print()

    return redirect('home')

@login_required
def sendComment(request, project_slug):
    form = CommentForm(request.POST or None)

    try: 
        soft = Soft.objects.get(slug=project_slug)
        if request.method == 'POST':
            if form.is_valid():
                form.instance.author = request.user
                form.instance.soft = soft
                form.save()

        comments = soft.comment_set.all()
        return redirect('/project/'+project_slug)
    except:
        print()

    try: 
        ebook = Ebook.objects.get(slug=project_slug)
        if request.method == 'POST':
            if form.is_valid():
                form.instance.author = request.user
                form.instance.ebook = ebook
                form.save()

        comments = ebook.comment_set.all()
        return redirect('/project/'+project_slug)
    except:
        print()

    return redirect('home')
