from django.urls import path

from . import views

urlpatterns = [
    # guest
    path('', views.home, name='home'),
    path('project/<project_slug>', views.project, name="project"),
    path('projects/<type_content>', views.projects, name="projects"),

    # user logged
    path('dashboard/', views.dashboard, name="dashboard"),

    # ebook
    path('createebook/', views.createEbook, name="createebook"),
    path('editebook/<int:ebook_id>', views.updateEbook, name="editebook"),
    path('deletebook/<int:ebook_id>', views.deleteEbook, name="deleteebook"),

    # software
    path('createsoft/', views.createSoft, name="createsoft"),
    path('editesoft/<int:soft_id>', views.updateSoft, name="editesoft"),
    path('deletesoft/<int:soft_id>', views.deleteSoft, name="deletesoft"),
]