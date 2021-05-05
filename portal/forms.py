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
            "file_name": "Arquivo",
        }
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "content",
            "versions", "file_name",
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
            "file_name": "Arquivo",
        }

        widgets = {
 
        }
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "keyword", 
            "qtd_pages", "content", 
            "edition", "file_name",
        ]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        labels  = {
            "id": "",
            "comment": "Faça um comentário",
        }

        fields = [
            "id", "comment"
        ]