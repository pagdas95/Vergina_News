# Generated by Django 4.0.4 on 2022-08-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_subcategory_options_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
