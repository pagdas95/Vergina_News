# Generated by Django 4.0.4 on 2023-05-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0015_alter_author_prof_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
