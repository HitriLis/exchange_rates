from django.db import models


class ExchangeRates(models.Model):
    google_sheets_id = models.CharField(max_length=150, null=True, blank=True, verbose_name='Номер в таблице')
    order = models.CharField(max_length=150, verbose_name='Заказ №')
    price = models.CharField(max_length=150, null=True, blank=True, verbose_name='Стоимость')
    delivery_time = models.CharField(max_length=150, null=True, blank=True, verbose_name='Срок поставки')
    exchange_rate = models.CharField(max_length=150, null=True, blank=True, verbose_name='Обменный курс')

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курс валют'
