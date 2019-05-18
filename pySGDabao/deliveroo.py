import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup
import json

from pySGDabao.utils import *

class Deliveroo:
    def __init__(self, postal_code, base_url="https://deliveroo.com.sg/"):
        self.postal_code = postal_code
        self.base_url = base_url
        self.raw_restaurants = self.scrape_restaurants()
        self.restaurant_index = self.index_restaurants()
        
    def scrape_restaurants(self):
        """Return a list of raw restaurant information listed by Deliveroo"""
        params = {
            "postcode": str(self.postal_code)
        }
        url = urljoin(self.base_url, "restaurants/singapore/q")

        html = requests.get(url=url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        data = json.loads(soup.find(id='__NEXT_DATA__').string)['props']['initialState']['home']['feed']['results']['data']
        
        restaurants = []
        if data:
            for UILayoutList in [i for i in data if i['typeName'] == 'UILayoutList']:
                for block in UILayoutList['blocks']:
                    if block['typeName'] == 'UIRestaurant':
                        restaurants.append(block['restaurant'])

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
        return self.raw_restaurants[index]["links"]["self"]["href"]

    def scrape_menu(self, restaurant_name):
        """Return a list of raw menu information by the given restaurant"""
        url = self.get_url(restaurant_name)
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, 'html.parser')
        return json.loads(soup.find("script", {"class":"js-react-on-rails-component"}).contents[0])

    def get_menu_items(self, restaurant_name):
        """Return a list of menu items by the given restaurant"""
        raw_menu = self.scrape_menu(restaurant_name)

        menu_items = []

        for product in raw_menu['menu']['items']:
            item = {
                "name": xstr(product["name"]),
                "description": xstr(product["description"]),
                "price": xstr(product["raw_price"]),
                "image": xstr(product["image"]),
            }

            menu_items.append(item)
        
        return menu_items