import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup
import json

from pySGDabao.utils import *

class Honestbee:
    def __init__(self, postal_code, base_url="https://www.honestbee.sg/"):
        self.postal_code = postal_code
        self.base_url = base_url
        self.raw_restaurants = self.scrape_restaurants()
        self.restaurant_index = self.index_restaurants()

    def scrape_restaurants(self):
        """Return a list of raw restaurants' information listed by HonestBee"""
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
        url = urljoin(self.base_url, "api/api/brands")

        while True:
            params["page"] = pageNo
            req = requests.get(url=url, params=params).json()
            for restaurant in req:
                restaurants.append(restaurant)

            if len(req) != 48:
                break
            
            pageNo += 1
        
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
        return urljoin(self.base_url, "food/restaurants" + "/" + self.raw_restaurants[index]["slug"])
    
    def scrape_menu(self, restaurant_name):
        """Return a list of raw menu information by the given restaurant"""
        url = self.get_url(restaurant_name)
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, 'html.parser')
        line = soup.findAll("script")[0].contents[0]
        return json.loads(line[line.find("=")+1: line.find(";\n")])

    def get_menu_items(self, restaurant_name):
        """Return a list of menu items by the given restaurant"""
        raw_menu = self.scrape_menu(restaurant_name)

        menu_items = []

        for product in raw_menu["food"]["products"]["byId"].values():
            item = {
                "name": xstr(product["title"]),
                "description": xstr(product["description"]),
                "price": xstr(product["price"]),
                "image": xstr(product["imageUrl"])
            }

            menu_items.append(item)
        
        return menu_items