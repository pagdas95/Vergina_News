# Generated by Django 4.0.4 on 2022-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='job_title',
            field=models.CharField(choices=[('1', 'Sports'), ('2', 'People'), ('3', 'Auto'), ('4', 'Culture'), ('5', 'Politics'), ('6', 'Society'), ('7', 'Business'), ('8', 'Economy')], max_length=10),
        ),
    ]