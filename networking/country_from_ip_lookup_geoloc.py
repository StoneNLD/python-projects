#!/usr/bin/env python

import urllib.request
import json

loc = "84.81.214.69" 

with urllib.request.urlopen(f"https://geolocation-db.com/jsonp/{loc}") as url:
    data = url.read().decode()
    data = data.split("(")[1].strip(")")
    data = json.loads(data)

country_name = data['country_name']
city = data['city']
ip = data['IPv4']

print(f'The IP {ip} is located in {city} in {country_name}')
