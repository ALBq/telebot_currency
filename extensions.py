import json
import requests
from config import keys


class APIException(Exception):
    pass


class ExchangeRatesAPI:
    @staticmethod
    def get_price(base: str, quote: str, amount: float):
        if not (base in keys) or \
            not (quote in keys):
            raise APIException(f'Не удаётся найти валюту {base}')

        if (not isinstance(amount, float)) and (not isinstance(amount, int)):
            raise APIException(f'Не удаётся перевести {amount} в число.')
        iso_currency = f'{keys[base]}_{keys[quote]}'
        r = requests.get(
            f'https://free.currconv.com/api/v7/convert?q={iso_currency}&compact=ultra&apiKey=10aab0bf0e49ec92a94c'
        )
        result = json.loads(r.content).get(iso_currency)

        return result * amount
