# Generated by Django 3.0.3 on 2020-02-16 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_title', models.CharField(max_length=70, verbose_name='Название:')),
                ('serial_url_video',
                 models.CharField(max_length=170, verbose_name='Embeded ссылка на видео в YouTube:')),
                ('serial_url_poster', models.CharField(max_length=170, verbose_name='Ссылка на постер:')),
                ('serial_year', models.IntegerField(verbose_name='Год выхода:')),
                ('serial_rating', models.FloatField(verbose_name='Рейтинг:')),
                ('serial_director', models.CharField(max_length=50, verbose_name='Режиссер:')),
                ('serial_desc', models.CharField(max_length=850, verbose_name='Описание:')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации:')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=50, verbose_name='Автор:')),
                ('comment_text', models.CharField(max_length=80, verbose_name='Текст комментария:')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serials.Serial')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
