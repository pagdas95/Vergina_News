# Generated by Django 4.0.4 on 2022-06-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_category_alter_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sub_category',
            field=models.TextField(choices=[(1, 'Champions League')], null=True),
        ),
    ]
