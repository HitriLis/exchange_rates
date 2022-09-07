from typing import List
from pydantic import BaseModel


class ExchangeRateBaseScheme(BaseModel):
    google_sheets_id: str
    order: str
    price: str
    delivery_time: str
    exchange_rate: str


class ExchangeRateScheme(ExchangeRateBaseScheme):
    id: int


class ExchangeRateSchemeList(BaseModel):
    exchanges: List[ExchangeRateScheme] = []
