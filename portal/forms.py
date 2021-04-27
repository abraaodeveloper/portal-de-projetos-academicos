from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["id", "title", "resume", "slug", "type_content", "language", "keyword", "qtd_pages", "content"]
