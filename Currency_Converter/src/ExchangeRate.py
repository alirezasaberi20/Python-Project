import os
import requests
from cachetools import cached, TTLCache

ttl_cache = TTLCache(maxsize=162, ttl=60*60*6)

API_Key = os.environ['EXCHANGE_RATE_API_KEY']

def check_API_status():
    response = requests.get(url=f'https://v6.exchangerate-api.com/v6/{API_Key}/latest/USD')
    if response.status_code != 200:
        return 'Error'
    return 'API is working'


@cached(ttl_cache)
def Currency_Converter(Amount, BaseCurency='USD', TargetCurrency='EUR'):
    response = requests.get(url=f'https://v6.exchangerate-api.com/v6/{API_Key}/latest/{BaseCurency}')
    if response.status_code != 200:
        return 'Error'
    response_values = response.json()
    currency_rate = response_values['conversion_rates']
    return Amount * currency_rate[TargetCurrency]

 