# Generated by Django 4.2.2 on 2023-07-09 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='short_description',
        ),
    ]