#!/usr/bin/env python

import pygeoip

gi = pygeoip.GeoIP('GeoIP.dat')
gi.country_code_by_name('google.com')


