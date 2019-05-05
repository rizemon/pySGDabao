import requests

from pySGDabao.utils import get_latt_long, pretty_format

class Foodpanda:
    def __init__(self, postal_code, url="https://sg.fd-api.com/"):
        self.postal_code = postal_code
        self.url = url
        self.raw_listing = self.get_listing()
        self.json = self.parse_listing()

    def get_listing(self):
        """Return a list of restaurant information listed by Foodpanda"""
        latitude, longitude = get_latt_long(self.postal_code)

        params = {
            "latitude": latitude,
            "longitude": longitude,
        }
        headers = {
            "X-FP-API-KEY": "volo"
        }

        restaurants = requests.get(url=self.url + "api/v5/vendors", params=params, headers=headers).json()['data']['items']

        return restaurants
    
    def parse_listing(self):
        return {
            restaurant["name"]: {
                "url": restaurant["web_path"]
            }
            for restaurant in self.raw_listing
        }