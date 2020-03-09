import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class News(models.Model):
    news_title = models.CharField('Название:', max_length=70)
    news_text = models.TextField('Текст новости:')

    pub_date = models.DateTimeField('Дата публикации:')

    def __str__(self):
        return self.news_title

    def was_pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=3))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name_author = models.CharField('Автор:', max_length=50)
    comment_text = models.CharField('Текст комментария:', max_length=80)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
