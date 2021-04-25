from django.urls import path

from . import views

urlpatterns = [
    # guest
    path('', views.home, name='home'),
    path('project/<post_slug>', views.project, name="project"),

    # user logged
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createpost/', views.createPost, name="createpost"),
]