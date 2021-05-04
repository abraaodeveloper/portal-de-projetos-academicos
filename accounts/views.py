from django.shortcuts import  render, redirect
from django.views import generic
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
	form_class = NewUserForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')