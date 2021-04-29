from django.urls import path

from . import views

urlpatterns = [
    # guest
    path('', views.home, name='home'),
    path('project/<soft_slug>', views.project, name="project"),
    path('projects/<type_content>', views.projects, name="projects"),

    # user logged
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createsoft/', views.createSoft, name="createsoft"),
]