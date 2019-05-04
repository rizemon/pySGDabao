from bs4 import BeautifulSoup
import requests
import json

from pySGDabao.utils import get_latt_long

DELIVEROO_URL = "https://deliveroo.com.sg/restaurants/singapore/q"

def get_listing(postal_code):
    """Return a list of restaurant names listed by Deliveroo"""
    params = {
        "postcode": str(postal_code)
    }

    html = requests.get(url=DELIVEROO_URL, params=params).content
    soup = BeautifulSoup(html, 'html.parser')
    data = json.loads(list(soup.findAll('script'))[4].contents[0][len("__NEXT_DATA__ = "):-len(";__NEXT_LOADED_PAGES__=[];__NEXT_REGISTER_PAGE=function(r,f){__NEXT_LOADED_PAGES__.push([r, f])}")])['props']['initialState']['home']['feed']['results']['data']
    
    restaurants = []
    if data:
        for UILayoutList in [i for i in data if i['typeName'] == 'UILayoutList']:
            for block in UILayoutList['blocks']:
                if block['typeName'] == 'UIRestaurant':
                    restaurants.append(block['restaurant'])

    return restaurants