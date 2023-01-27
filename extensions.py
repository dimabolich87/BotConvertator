import requests
import json
from config import *

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = keys[base]
        except KeyError:
            raise APIException(f'валюта {base} не найдена')

        try:
            sym_key = keys[sym]
        except KeyError:
            raise APIException(f'валюта {sym} не найдена')

        if base_key == sym_key:
            raise APIException(f'не получится перевести валюту в себя {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'не получилось обработать колличество {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}")
        resp = json.loads(r.content)
        new_price = resp[sym_key] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message


