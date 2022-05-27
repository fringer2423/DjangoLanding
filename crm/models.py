from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    order_data = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    order_name = models.CharField(max_length=30, verbose_name="Название")
    order_phone = models.CharField(max_length=15, verbose_name="Телефон")

    def __str__(self):
        return self.order_name
