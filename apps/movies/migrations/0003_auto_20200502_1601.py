# Generated by Django 3.0.5 on 2020-05-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200311_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_url_video',
            field=models.CharField(max_length=170, verbose_name='ID видео на YouTube:'),
        ),
    ]
