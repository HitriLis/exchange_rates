from vendors import AuthGoogleVendor


class GoogleSheetsApi(AuthGoogleVendor):

    def __init__(self, spreadsheet_id: str, credential_file: str, scopes: list):
        super().__init__(credential_file, scopes)
        self.service = self._service()
        self.spreadsheet_id = spreadsheet_id

    def get_data(self, range_sheet: str = 'Лист номер один!B2:D5', major_dimension: str = 'ROWS') -> dict:
        result = {}
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_sheet,
                majorDimension=major_dimension
            ).execute()
        except BaseException as err:
            print(err)
        return result


google_sheets_connector = GoogleSheetsApi(
    spreadsheet_id="199p_MgfaQcfWoACDh-TIHet2ypH__M0mmOoYfcgnetk",
    credential_file="jkjkj.json",
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
