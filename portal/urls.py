from django.urls import path

from .views.dashboard_views import *
from .views.ebook_views import *
from .views.guest_views import *
from .views.soft_views import *

urlpatterns = [
    # guest
    path('', home, name='home'),
    path('project/<project_slug>', project, name="project"),
    path('projects/<type_content>', projects, name="projects"),
    path('getstatistic/', getStatiscs, name="getstatistic"),

    path('sendcomment/<project_slug>', sendComment, name="sendcomment"),
    path('about/', about, name="about"),

    # user logged
    path('dashboard/', dashboard, name="dashboard"),

    # ebook
    path('createebook/', createEbook, name="createebook"),
    path('editebook/<int:ebook_id>', updateEbook, name="editebook"),
    path('deletebook/<int:ebook_id>', deleteEbook, name="deleteebook"),

    # software
    path('createsoft/', createSoft, name="createsoft"),
    path('editesoft/<int:soft_id>', updateSoft, name="editesoft"),
    path('deletesoft/<int:soft_id>', deleteSoft, name="deletesoft"),
]