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
                if not cache.get('update_quotes'):
                    cache.set('update_quotes', 1, 3600 * 24)
                    value_currency = currency_quotes.get_quote()
                    for i in exchange_data:
                        i.exchange_rate = round(value_currency * i.price, 2)
                    ExchangeRates.objects.bulk_update(list(exchange_data), ['exchange_rate'])
                print('currency_quotes.get_quote()')



            time.sleep(5)  # Sleep for 5 seconds
