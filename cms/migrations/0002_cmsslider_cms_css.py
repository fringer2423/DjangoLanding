# Generated by Django 4.0.4 on 2022-05-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='carousel-item', max_length=200, verbose_name='CSS'),
        ),
    ]