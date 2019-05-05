import requests

from pySGDabao.utils import get_latt_long, pretty_format

class Honestbee:
    def __init__(self, postal_code, url="https://www.honestbee.sg/"):
        self.postal_code = postal_code
        self.url = url
        self.raw_listing = self.get_listing()

    def get_listing(self):
        """Return a list of restaurant names listed by HonestBee"""
        latitude, longitude = get_latt_long(self.postal_code)

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
            req = requests.get(url=self.url + "api/api/brands", params=params).json()
            for restaurant in req:
                restaurants.append(restaurant)

            if len(req) != 48:
                break
            
            pageNo += 1

        return restaurants
    
    def parse_listing(self):
        return {
            restaurant["name"]: {
                "url": self.url + "food/restaurants/" + restaurant["slug"]
            }
            for restaurant in self.raw_listing
        }