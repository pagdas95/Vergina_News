# Generated by Django 4.0.4 on 2022-09-08 13:01

import VerginaNews.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0032_alter_article_article_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_pic',
            field=models.ImageField(blank=True, upload_to=VerginaNews.utils.get_img_path, validators=[VerginaNews.utils.image_size_validator]),
        ),
    ]