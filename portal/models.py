from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Soft(models.Model):

    LANGUAGE = (
        ('Portuguese', 'Portuguese'),
        ('English', 'English')
    )

    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    slug = models.SlugField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    versions = models.IntegerField(default=0)
    language = models.CharField(max_length=12,  choices=LANGUAGE) 
    file_name = models.FileField(upload_to='books/files/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

class Ebook(models.Model):

    LANGUAGE = (
        ('Portuguese', 'Portuguese'),
        ('English', 'English')
    )

    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    slug = models.SlugField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    edition = models.IntegerField(default=0)
    language = models.CharField(max_length=12,  choices=LANGUAGE) 
    keyword = models.CharField(max_length=255)
    qtd_pages = models.IntegerField()
    file_name = models.FileField(upload_to='books/files/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title        