import requests
from django.shortcuts import render
from .models import CryptoPrice

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,avalanche-2",
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_7d_change": "true"
    }
    response = requests.get(url, params=params).json()

    btc_price = response['bitcoin']['usd']
    btc_change_24h = response['bitcoin'].get('usd_24h_change', 0)
    btc_change_7d = response['bitcoin'].get('usd_7d_change', 0)

    eth_price = response['ethereum']['usd']
    eth_change_24h = response['ethereum'].get('usd_24h_change', 0)
    eth_change_7d = response['ethereum'].get('usd_7d_change', 0)

    avax_price = response['avalanche-2']['usd']
    avax_change_24h = response['avalanche-2'].get('usd_24h_change', 0)
    avax_change_7d = response['avalanche-2'].get('usd_7d_change', 0)

    CryptoPrice.objects.create(name='BTC', price=btc_price, change_24h=btc_change_24h, change_7d=btc_change_7d)
    CryptoPrice.objects.create(name='ETH', price=eth_price, change_24h=eth_change_24h, change_7d=eth_change_7d)
    CryptoPrice.objects.create(name='AVAX', price=avax_price, change_24h=avax_change_24h, change_7d=avax_change_7d)

def home(request):
    fetch_crypto_prices()
    btc = CryptoPrice.objects.filter(name='BTC').order_by('-timestamp').first()
    eth = CryptoPrice.objects.filter(name='ETH').order_by('-timestamp').first()
    avax = CryptoPrice.objects.filter(name='AVAX').order_by('-timestamp').first()
    return render(request, 'prices/home.html', {'btc': btc, 'eth': eth, 'avax': avax})
