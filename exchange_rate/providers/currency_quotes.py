import xmltodict
import requests
from datetime import datetime
from datetime import timedelta


class CurrencyQuotes:

    def __init__(self):
        self.base_url = 'https://www.cbr.ru/scripts/XML_dynamic.asp'

    def __call(self, params: dict = None):
        try:
            response = requests.get(self.base_url, params=params)
        except Exception as error:
            print(error)
            return False
        return xmltodict.parse(response.content)

    def get_quote(self) -> float:
        now = datetime.now()
        date_req1 = now - timedelta(days=1)
        result = self.__call(params={
                'date_req1': date_req1.strftime('%d/%m/%Y'),
                'date_req2': now.strftime('%d/%m/%Y'),
                'VAL_NM_RQ': 'R01235'
            })
        val_curs = result.get('ValCurs', {}).get('Record', {}).get('Value', '')
        str_val = val_curs.split(',')
        return round(float('.'.join(str_val)), 2) if bool(val_curs) else 0


currency_quotes = CurrencyQuotes()
