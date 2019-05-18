import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup
import json

from pySGDabao.utils import *

class Foodpanda:
    def __init__(self, postal_code, base_url="https://sg.fd-api.com/"):
        self.postal_code = postal_code
        self.base_url = base_url
        self.raw_restaurants = self.scrape_restaurants()
        self.restaurant_index = self.index_restaurants()

    def scrape_restaurants(self):
        """Return a list of raw restaurants' information listed by Foodpanda"""
        latitude, longitude = get_latt_long(self.postal_code)

        params = {
            "latitude": latitude,
            "longitude": longitude,
        }
        headers = {
            "X-FP-API-KEY": "volo"
        }
        url = urljoin(self.base_url, "api/v5/vendors")

        restaurants = requests.get(url=url, params=params, headers=headers).json()['data']['items']

        return restaurants
    
    def index_restaurants(self):
        """Return a dictionary of restaurant names mapped to their respective index"""
        return { restaurant["name"]: idx  for idx, restaurant in enumerate(self.raw_restaurants)}

    def get_restaurant_names(self):
        """Return a list of restaurant names"""
        return list(self.restaurant_index.keys())
    
    def get_url(self, restaurant_name):
        """Return the URL of a given restaurant"""
        index = self.restaurant_index[restaurant_name]
        return self.raw_restaurants[index]["web_path"]

    def scrape_menu(self, restaurant_name):
        """Return a list of raw menu information by the given restaurant"""
        url = self.get_url(restaurant_name)
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, 'html.parser')
        return json.loads(soup.find("div", {"class":"where-wrapper"} )['data-vendor'])

    def get_menu_items(self, restaurant_name):
        """Return a list of menu items by the given restaurant"""
        raw_menu = self.scrape_menu(restaurant_name)

        menu_items = []

        for category in raw_menu['menus'][0]['menu_categories']:
            for product in category["products"]:
                item = {
                    "name": xstr(product["name"]),
                    "description": xstr(product["description"]),
                    "price": xstr(product["product_variations"][0]["price"]),
                    "image": ""
                }

                menu_items.append(item)
        
        return menu_items



        