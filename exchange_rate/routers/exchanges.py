from fastapi.responses import JSONResponse
from crm.myglobal import router
from exchange_rate.models import ExchangeRates
from exchange_rate.schemes import ExchangeRateSchemeList
from api.schemes import BodyMessage
from exchange_rate.google_sheets import google_sheets_connector

@router.get("/exchange-list/", tags=["Exchange"],
            responses={200: {"model": ExchangeRateSchemeList}, 400: {"model": BodyMessage}})
async def exchanges_list():
    """
        Получить список со всеми типами объекта:
    """
    print(google_sheets_connector.get_data())
    result = ExchangeRates.objects.values(
        'id',
    )
    return JSONResponse(status_code=200, content=ExchangeRateSchemeList(exchanges=list(result)).dict())
