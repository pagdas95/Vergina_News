# Generated by Django 4.0.4 on 2022-06-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
    ]
