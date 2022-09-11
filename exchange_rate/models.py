from django.db import models
from .utils import str_to_datetime


class ExchangeRatesManager(models.Manager):

    @staticmethod
    def get_list_values_from_google_data(values: tuple, idx: int) -> tuple:
        """
           Метод получения списка значений по индексу
        """
        return tuple(item[idx] for item in values)

    @staticmethod
    def validate_data_values(values: tuple):
        pattern = {
            'google_sheets_id': int,
            'order': int,
            'price': float,
            'delivery_time': str_to_datetime
        }
        result = []
        for item in values:
            data = {}
            for idx, key in enumerate(pattern.keys()):
                try:
                    data[key] = pattern[key](item[idx])
                except ValueError:
                    continue
            if bool(data):
                result.append(data)
        return tuple(result)


class ExchangeRates(models.Model):
    google_sheets_id = models.IntegerField(verbose_name='Номер в таблице')
    order = models.IntegerField(verbose_name='Заказ №')
    price = models.FloatField(verbose_name='Стоимость')
    delivery_time = models.DateTimeField(null=True, blank=True, verbose_name='Срок поставки')
    exchange_rate = models.FloatField(verbose_name='Обменный курс')
    objects = ExchangeRatesManager()

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курс валют'
