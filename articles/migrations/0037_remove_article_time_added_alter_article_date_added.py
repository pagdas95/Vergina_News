# Generated by Django 4.0.4 on 2023-05-28 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0036_article_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='time_added',
        ),
        migrations.AlterField(
            model_name='article',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 28, 18, 56, 17, 211749), verbose_name='Date'),
        ),
    ]
