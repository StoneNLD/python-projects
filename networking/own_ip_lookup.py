#!/usr/bin/env python

import re
import json
import urllib3

url = 'http://ipinfo.io/json'
http = urllib3.PoolManager()
r = http.request('GET', url)
data = json.loads(r.data.decode('utf-8'))

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print(f'IP : {4} \nRegion : {IP} \nCountry : {country} \nCity : {region} \nOrg : {org}')