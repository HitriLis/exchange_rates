from fastapi.responses import JSONResponse
from crm.myglobal import router
from exchange_rate.models import ExchangeRates
from exchange_rate.schemes import ExchangeRateScheme, ExchangeRateSchemeList
from api.schemes import BodyMessage


@router.get("/exchange-list/", tags=["Exchange"],
            responses={200: {"model": ExchangeRateSchemeList}, 400: {"model": BodyMessage}})
async def realty_list():
    """
        Получить список со всеми типами объекта:
    """
    result = ExchangeRates.objects.values(
        'id',
    )
    return JSONResponse(status_code=200, content=ExchangeRateSchemeList(exchanges=list(result)).dict())
