from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages

def SignUpView(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Prontinho! registrado. Aproveite!" )
			return redirect("main:homepage")
		messages.error(request, "Ops! Tente Novamente. informações inválidas.")
	form = NewUserForm
	return render (request=request, template_name="registration/signup.html", context={"form":form})