from bs4 import BeautifulSoup
import requests
import json

from pySGDabao.utils import get_latt_long, pretty_format

class Deliveroo:
    def __init__(self, postal_code, url="https://deliveroo.com.sg/"):
        self.postal_code = postal_code
        self.url = url
        self.raw_listing = self.get_listing()

    def get_listing(self):
        """Return a list of restaurant information listed by Deliveroo"""
        params = {
            "postcode": str(self.postal_code)
        }

        html = requests.get(url=self.url + "restaurants/singapore/q", params=params).content
        soup = BeautifulSoup(html, 'html.parser')
        data = json.loads(list(soup.findAll('script'))[4].contents[0][len("__NEXT_DATA__ = "):-len(";__NEXT_LOADED_PAGES__=[];__NEXT_REGISTER_PAGE=function(r,f){__NEXT_LOADED_PAGES__.push([r, f])}")])['props']['initialState']['home']['feed']['results']['data']
        
        restaurants = []
        if data:
            for UILayoutList in [i for i in data if i['typeName'] == 'UILayoutList']:
                for block in UILayoutList['blocks']:
                    if block['typeName'] == 'UIRestaurant':
                        restaurants.append(block['restaurant'])

        return restaurants
    
    def parse_listing(self):
        return {
            restaurant["name"]: {
                "url": restaurant["links"]["self"]["href"]
            }
            for restaurant in self.raw_listing
        }

    
