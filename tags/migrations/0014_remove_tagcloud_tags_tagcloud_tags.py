# Generated by Django 4.0.4 on 2023-05-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0013_alter_tagcloud_options_remove_tagcloud_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagcloud',
            name='tags',
        ),
        migrations.AddField(
            model_name='tagcloud',
            name='tags',
            field=models.ManyToManyField(to='tags.tags'),
        ),
    ]
