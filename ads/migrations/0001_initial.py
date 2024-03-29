# Generated by Django 4.0.4 on 2022-07-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('ad_pic', models.ImageField(upload_to='ads_pics')),
                ('url', models.URLField(max_length=256)),
                ('total_views', models.IntegerField(default=0)),
            ],
        ),
    ]
