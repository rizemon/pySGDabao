import requests
import json
import re

def get_latt_long(postal_code):
    """Return a tuple containing the latitude and longitude of the given postal code"""
    req = requests.get(
        url = "https://geocode.xyz/" + str(postal_code),
        params= {
            "geoit":"JSON"
        },
        cookies = {
            "xyzh": "xyzh"
        }
    ).json()
    return req['latt'], req['longt']

def pretty_format(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)