from django.contrib import admin

from portal.models import Soft, Ebook

admin.site.site_header = 'Portal de Projetos Acadêmicos'
admin.site.index_title = 'Aqui voçê pode gerenciar todos os projetos!'
admin.site.site_title = 'Administração'

# Register your models here.
admin.site.register(Soft)
admin.site.register(Ebook)