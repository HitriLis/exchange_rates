from vendors import AuthGoogleVendor
from googleapiclient.errors import HttpError


class GoogleSheetsApi(AuthGoogleVendor):

    def __init__(self, spreadsheet_id: str, credential_file: str, scopes: list):
        super().__init__(credential_file, 'sheets', scopes)
        self.service = self._service()
        self.spreadsheet_id = spreadsheet_id

    def get_data_sheets(self, ranges_sheet: list, major_dimension: str = 'ROWS') -> dict:

        result = {}
        try:
            result = self.service.spreadsheets().values().batchGet(
                spreadsheetId=self.spreadsheet_id,
                ranges=ranges_sheet,
                majorDimension=major_dimension
            ).execute()
        except HttpError as err:
            print(err)
        return result

    def get_all_sheets(self) -> list:
        result = {}
        try:

            result = self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id,
            ).execute()
        except HttpError as err:
            print(err)
        return result.get('sheets', [])
