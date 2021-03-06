# Generated by Django 4.0.4 on 2022-05-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Chat id')),
                ('tg_message', models.CharField(max_length=200, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Настройка телебота',
                'verbose_name_plural': 'Настройки телебота',
            },
        ),
    ]
