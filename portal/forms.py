from django import forms
from .models import *

class SoftForm(forms.ModelForm):

    class Meta:
        model = Soft
        labels  = {
            "id": "",
            "title": "Título",
            "resume" : "Resumo", 
            "slug": "Slug", 
            "language": "Linguagem", 
            "content": "Conteúdo principal", 
            "versions": "Versão",
        }
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "content",
            "versions"
        ]

class EbookForm(forms.ModelForm):
    
    class Meta:
        model = Ebook
        labels  = {
            "id": "",
            "title": "Título",
            "resume" : "Resumo", 
            "slug": "Slug", 
            "language": "Linguagem", 
            "keyword": "Palavras Chave", 
            "qtd_pages": "Quantidade de páginas", 
            "content": "Conteúdo principal", 
            "edition": "Edição",
        }
        prepopulated_fields = {"slug": ("title",)}
        widgets = {
 
        }
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "keyword", 
            "qtd_pages", "content", 
            "edition"
        ]