# Generated by Django 4.0.4 on 2022-08-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_subcategory_options_alter_category_slug_and_more'),
        ('tags', '0004_tags_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
