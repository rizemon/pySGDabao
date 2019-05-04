import requests

from pySGDabao.utils import get_latt_long

HONESTBEE_URL = "https://www.honestbee.sg/api/api/brands"

def get_listing(postal_code):
    """Return a list of restaurant names listed by HonestBee"""
    latitude, longitude = get_latt_long(postal_code)

    restaurants = []
    pageNo = 1

    params = {
        "countryCode": "SG",
        "serviceType": "food",
        "latitude": latitude,
        "longitude": longitude,
        "page": 1,
    }
    while True:
        params["page"] = pageNo
        req = requests.get(url=HONESTBEE_URL, params=params).json()
        for restaurant in req:
            restaurants.append(restaurant)

        if len(req) != 48:
            break
        
        pageNo += 1

    return restaurants