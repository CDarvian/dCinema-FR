import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Serial(models.Model):
    serial_title = models.CharField('Название:', max_length=70)

    serial_url_video = models.CharField('Embeded ссылка на видео в YouTube:', max_length=170)
    serial_url_poster = models.CharField('Ссылка на постер:', max_length=170)

    serial_year = models.IntegerField('Год выхода:')
    serial_rating = models.FloatField('Рейтинг:')
    serial_director = models.CharField('Режиссер:', max_length=50)

    serial_desc = models.CharField('Описание:', max_length=850)

    pub_date = models.DateTimeField('Дата публикации:')

    def __str__(self):
        return self.serial_title

    def was_pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=3))

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'


class Comment(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
    name_author = models.CharField('Автор:', max_length=50)
    comment_text = models.CharField('Текст комментария:', max_length=80)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
