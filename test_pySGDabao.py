from pySGDabao import *
from pySGDabao import utils

from bs4 import BeautifulSoup
import requests

import json

def main():
    postal_code = 760625
    test_foodpanda = Foodpanda(postal_code)
    test_deliveroo = Deliveroo(postal_code)
    test_honestbee = Honestbee(postal_code)

    with open("foodpanda.json", "w") as f:
        f.write(utils.pretty_format(test_foodpanda.get_menu_items(test_foodpanda.get_restaurant_names()[0])))

    with open("deliveroo.json", "w") as f:
        f.write(utils.pretty_format(test_deliveroo.get_menu_items(test_deliveroo.get_restaurant_names()[0])))

    with open("honestbee.json", "w") as f:
        f.write(utils.pretty_format(test_honestbee.get_menu_items(test_honestbee.get_restaurant_names()[0])))


if __name__ == "__main__":
    main()