from django.db import models


class CmsSlider(models.Model):
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    cms_img = models.ImageField(upload_to='sliderImg/', verbose_name='Изображение')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Описание')
    cms_css = models.CharField(max_length=200, verbose_name='CSS', default='carousel-item')


    def __str__(self):
        return self.cms_title