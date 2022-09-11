from vendors import AuthGoogleVendor
from googleapiclient.errors import HttpError


class GoogleSheetsApi(AuthGoogleVendor):

    def __init__(self, spreadsheet_id: str, credential_file: str, scopes: list):
        """
        Класс для работы с Google таблицами
        :param credential_file: Путь к файла с кредами
        :param scopes: Права доступа
        :param spreadsheet_id: Id Таблицы
        """
        super().__init__()
        self.credential_file = credential_file
        self.scopes = scopes
        self.api = 'sheets'
        self.service = self.service()
        self.spreadsheet_id = spreadsheet_id

    def get_data_sheets(self, ranges_sheet: list, major_dimension: str = 'ROWS', value_only: bool = True) -> list:

        """
            Метод получения списка таблиц
            :param ranges_sheet: Список страниц которые нужно получить
            :param major_dimension: Способ отображения данных ROWS или
            :param value_only: Список всех значений одним списком
        """

        result = []
        try:
            response = self.service.spreadsheets().values().batchGet(
                spreadsheetId=self.spreadsheet_id,
                ranges=ranges_sheet,
                majorDimension=major_dimension
            ).execute()
            result = response.get('valueRanges', [])
        except HttpError as err:
            print(err)
        if value_only:
            data = []
            for item in result:
                data += [t for t in item.get('values')]
            result = data
        return result

    def get_all_sheets(self, ranges_flat: bool = False) -> list:
        """
            Метод получения списка листов в Google таблицах
        """
        result = []
        try:
            result = self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id,
            ).execute().get('sheets', [])
        except HttpError as err:
            print(err)
        if ranges_flat and result:
            result = [i.get('properties').get('title') for i in result]

        return result
