from fastapi.responses import JSONResponse
from crm.myglobal import router
from exchange_rate.models import ExchangeRates
from exchange_rate.schemes import ExchangeRateSchemeList
from api.schemes import BodyMessage


@router.get("/exchange-list/", tags=["Exchange"],
            responses={200: {"model": ExchangeRateSchemeList}, 400: {"model": BodyMessage}})
async def exchanges_list():
    """
        Получить список со всеми типами объекта:
    """
    result = ExchangeRates.objects.values(
        'id',
        'google_sheets_id',
        'order',
        'price',
        'delivery_time',
        'exchange_rate'
    ).all()
    return JSONResponse(status_code=200, content=ExchangeRateSchemeList(exchanges=list(result)).dict())
