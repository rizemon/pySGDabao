# pySGDabao
A library for your Singapore food delivery needs

## Currently supports
* Foodpanda
* Deliveroo
* HonestBee

## Getting started
```python
from pySGDabao import * 

postal_code = 530511
foodpanda_client = Foodpanda(postal_code)
print(foodpanda_client.get_menu_items("KFC (Hougang Mall)"))

"""
[
    {
        "description": "1 HotBlaze Grilled Chicken, 3 pcs Nuggets, 1 side and 1 drink",
        "image": "",
        "name": "HotBlaze Grilled Meal",
        "price": 10.95
    },
    {
        "description": "1 HotBlaze Grilled Chicken, 3 pcs Chicken, 3 pcs Hot & Crispy Tenders, 2 sides and 2 drinks",
        "image": "",
        "name": "HotBlaze Grilled Buddy Meal",
        "price": 26.95
    },
    ...
]
"""
```

## Main Functions

### ```pySGDabao.Foodpanda(self, postal_code, base_url="https://sg.fd-api.com/")```
### ```pySGDabao.Deliveroo(self, postal_code, base_url="https://deliveroo.com.sg/")```
### ```pySGDabao.Honestbee(self, postal_code, base_url="https://www.honestbee.sg/")```
> Creates an object that stores information regarding the available restaurants located near the given postal code. If ```base_url``` is specified, all HTTP requests to be made will be relative to it.  

<br>

### ```pySGDabao.Foodpanda.get_restaurant_names()```
### ```pySGDabao.Deliveroo.get_restaurant_names()```
### ```pySGDabao.Honestbee.get_restaurant_names()```
> Gets a list of restaurant names near the given postal code

<br>

### ```pySGDabao.Foodpanda.get_url(restaurant_name)```
### ```pySGDabao.Deliveroo.get_url(restaurant_name)```
### ```pySGDabao.Honestbee.get_url(restaurant_name)```
> Gets the URL link to the given restaurant's page

<br>

### ```pySGDabao.Foodpanda.get_menu_items(restaurant_name)```
### ```pySGDabao.Deliveroo.get_menu_items(restaurant_name)```
### ```pySGDabao.Honestbee.get_menu_items(restaurant_name)```
> Gets a list of dictionaries comprising the name, description, price and image URL of each item sold by the given restaurant

<br>

## Advanced Functions

### ```pySGDabao.Foodpanda.scrape_restaurants()```
### ```pySGDabao.Deliveroo.scrape_restaurants()```
### ```pySGDabao.Honestbee.scrape_restaurants()```
> Returns the raw JSON from the website's search page

<br>

### ```pySGDabao.Foodpanda.scrape_menu(restaurant_name)```
### ```pySGDabao.Deliveroo.scrape_menu(restaurant_name)```
### ```pySGDabao.Honestbee.scrape_menu(restaurant_name)```
> Returns the raw JSON from the given restaurant's page