from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<post_slug>', views.project, name="project"),
]