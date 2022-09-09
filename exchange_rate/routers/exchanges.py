from fastapi.responses import JSONResponse
from crm.myglobal import router
from exchange_rate.models import ExchangeRates
from exchange_rate.schemes import ExchangeRateSchemeList
from api.schemes import BodyMessage
from exchange_rate.google_sheets import GoogleSheetsApi


@router.get("/exchange-list/", tags=["Exchange"],
            responses={200: {"model": ExchangeRateSchemeList}, 400: {"model": BodyMessage}})
async def exchanges_list():
    """
        Получить список со всеми типами объекта:
    """
    google_sheets_connector = GoogleSheetsApi(
        spreadsheet_id="199p_MgfaQcfWoACDh-TIHet2ypH__M0mmOoYfcgnetk",
        credential_file="credentials/321411-7817fc52db23.json",
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    ranges_sheet = [i.get('properties').get('title') for i in google_sheets_connector.get_all_sheets()]
    print(google_sheets_connector.get_data_sheets(ranges_sheet=ranges_sheet))
    result = ExchangeRates.objects.values(
        'id',
    )
    return JSONResponse(status_code=200, content=ExchangeRateSchemeList(exchanges=list(result)).dict())
