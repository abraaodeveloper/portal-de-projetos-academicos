from django import forms
from .models import *

class SoftForm(forms.ModelForm):

    class Meta:
        model = Soft
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "content",
            "versions"
        ]

class EbookForm(forms.ModelForm):

    class Meta:
        model = Ebook
        fields = [
            "id", "title",
            "resume", "slug", 
            "language", "keyword", 
            "qtd_pages", "content", 
            "edition"
        ]