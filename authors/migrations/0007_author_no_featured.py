# Generated by Django 4.0.4 on 2022-07-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_remove_author_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='no_featured',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=4, null=True),
        ),
    ]
