from django.db import models


class TeleSettings(models.Model):
    class Meta:
        verbose_name = 'Настройка телебота'
        verbose_name_plural = 'Настройки телебота'

    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Chat id')
    tg_message = models.CharField(max_length=200, verbose_name='Сообщение')

    def __str__(self):
        return self.tg_message
