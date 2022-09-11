import time
from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django.db.models import F
from exchange_rate.models import ExchangeRates
from exchange_rate.providers.google_sheets_api import GoogleSheetsApi
from exchange_rate.providers.currency_quotes import currency_quotes
from exchange_rate.utils import google_values_to_tuple


class Command(BaseCommand):
    help = 'Команда сбора данных из google таблиц'

    def handle(self, *args, **options):
        google_sheets_connector = GoogleSheetsApi(
            spreadsheet_id="199p_MgfaQcfWoACDh-TIHet2ypH__M0mmOoYfcgnetk",
            credential_file="credentials/321411-7817fc52db23.json",
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        while True:
            ranges_sheets = google_sheets_connector.get_all_sheets(ranges_flat=True)
            if ranges_sheets:
                data_sheets = google_values_to_tuple(
                    google_sheets_connector.get_data_sheets(ranges_sheet=ranges_sheets, value_only=True))
                exchange_data = ExchangeRates.objects.all()
                convert_data = ExchangeRates.objects.validate_data_values(data_sheets)

                if not exchange_data.exists():
                    value_currency = currency_quotes.get_quote()
                    bulk_data = [ExchangeRates(
                        **item,
                        exchange_rate=round(value_currency * item.get('price'), 2)
                            ) for item in convert_data]
                    ExchangeRates.objects.bulk_create(bulk_data)
                else:
                    print(currency_quotes.get_quote())
                    if not cache.get('update_quotes'):
                        value_currency = currency_quotes.get_quote()
                        cache.set('update_quotes', value_currency, 3600 * 24)
                        for i in exchange_data:
                            i.exchange_rate = round(value_currency * i.price, 2)
                        ExchangeRates.objects.bulk_update(list(exchange_data), ['exchange_rate'])
                    if convert_data:
                        temp_data = {i.order.__str__(): i for i in exchange_data}
                        data_update = []
                        for idx, item in enumerate(convert_data):
                            order = item.get('order').__str__()
                            if temp_data.get(order):
                                if not item == temp_data[order].get_dict_data():
                                    data_update.append(ExchangeRates(**item, id=temp_data[order].id))
                                del temp_data[order]
                            else:
                                value_currency = cache.get('update_quotes')
                                obj, created = ExchangeRates.objects.get_or_create(
                                    order=item.get('order'),
                                    defaults={
                                        **item,
                                        'exchange_rate': round(value_currency * item.get('price'), 2)
                                    })
                                print('not exists')
                        if temp_data.values():
                            test = [i.id for i in temp_data.values()]
                            ExchangeRates.objects.filter(pk__in=test).delete()
                        if data_update:
                            ExchangeRates.objects.bulk_update(data_update, ['delivery_time', 'price', 'google_sheets_id'])
            time.sleep(5)  # Sleep for 5 seconds
