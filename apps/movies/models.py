import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField('Название:', max_length=70)

    movie_url_video = models.CharField('Embeded ссылка на видео в YouTube:', max_length=170)
    movie_url_poster = models.CharField('Ссылка на постер:', max_length=170)

    movie_year = models.IntegerField('Год выхода:')
    movie_rating = models.FloatField('Рейтинг:')
    movie_director = models.CharField('Режиссер:', max_length=50)

    movie_desc = models.CharField('Описание:', max_length=850)

    pub_date = models.DateTimeField('Дата публикации:')

    def __str__(self):
        return self.movie_title

    def was_pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=3))

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name_author = models.CharField('Имя автора:', max_length=50)
    username_author = models.CharField('Имя пользователя автора:', max_length=60)
    comment_text = models.CharField('Текст комментария:', max_length=80)

    def __str__(self):
        return self.name_author + ' - ' + self.username_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
