# Generated by Django 4.1 on 2022-09-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangerates',
            name='is_expired',
            field=models.BooleanField(default=False, verbose_name='Срок обработки заказа истёк'),
        ),
    ]