# Generated by Django 4.0.4 on 2022-08-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_rename_tags_tags_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]
