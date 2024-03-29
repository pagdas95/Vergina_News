# Generated by Django 4.0.4 on 2022-08-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_subcategory_options_alter_category_slug_and_more'),
        ('tags', '0008_remove_tags_category_tags_category_alter_tags_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='category',
        ),
        migrations.AddField(
            model_name='tags',
            name='category',
            field=models.ManyToManyField(null=True, to='categories.category'),
        ),
        migrations.RemoveField(
            model_name='tags',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='tags',
            name='sub_category',
            field=models.ManyToManyField(null=True, to='categories.subcategory'),
        ),
    ]
