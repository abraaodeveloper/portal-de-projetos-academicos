# Generated by Django 3.1.7 on 2021-04-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]