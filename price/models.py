from django.db import models


class PriceCard(models.Model):
    class Meta:
        verbose_name = 'Цена в карточке'
        verbose_name_plural = 'Цены в карточках'

    pc_value = models.CharField(max_length=10, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_value


class PriceTable(models.Model):
    class Meta:
        verbose_name = 'Цена в таблице'
        verbose_name_plural = 'Цены в таблице'

    pt_title = models.CharField(max_length=100, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=10, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=10, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title
