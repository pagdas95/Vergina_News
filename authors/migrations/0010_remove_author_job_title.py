# Generated by Django 4.0.4 on 2022-08-20 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_alter_author_prof_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='job_title',
        ),
    ]
