# Generated by Django 3.1.7 on 2021-04-27 21:56

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('resume', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('type_content', models.CharField(choices=[('ebook', 'ebook'), ('software', 'software')], max_length=12)),
                ('language', models.CharField(choices=[('Portuguese', 'Portuguese'), ('English', 'English')], max_length=12)),
                ('keyword', models.CharField(max_length=255)),
                ('qtd_pages', models.IntegerField()),
                ('file_name', models.FileField(upload_to='books/files/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
