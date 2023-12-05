# Generated by Django 4.2.2 on 2023-07-04 04:17

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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_description', models.TextField(null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Programming', 'Programming'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Finance', 'Finance')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
