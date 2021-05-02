# Generated by Django 3.1.7 on 2021-05-02 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_auto_20210430_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('ebook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.ebook')),
                ('soft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.soft')),
            ],
        ),
    ]
