import requests

from pySGDabao.utils import get_latt_long

FOODPANDA_URL = "https://sg.fd-api.com/api/v5/vendors"

def get_listing(postal_code):
    """Return a list of restaurant names listed by Foodpanda"""
    latitude, longitude = get_latt_long(postal_code)

    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    headers = {
        "X-FP-API-KEY": "volo"
    }

    restaurants = requests.get(url=FOODPANDA_URL, params=params, headers=headers).json()['data']['items']

    return restaurants