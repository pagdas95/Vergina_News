# Generated by Django 4.0.4 on 2022-08-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_alter_article_article_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]