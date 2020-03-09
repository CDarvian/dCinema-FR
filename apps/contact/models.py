from django.db import models


# Create your models here.

class Ticket(models.Model):
    ticket_name = models.CharField('Имя отправителя:', max_length=50)
    ticket_email = models.CharField('Почта отправителя:', max_length=70)

    ticket_text = models.TextField('Сообщение отправителя:')

    def __str__(self):
        return self.ticket_name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
