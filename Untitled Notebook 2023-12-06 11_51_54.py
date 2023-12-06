# Databricks notebook source
import googlemaps
from datetime import datetime

key='AIzaSyAb5MLQaoMau6INaHQFCbq1PhwIjgKv0Io'

gmaps = googlemaps.Client(key='AIzaSyAb5MLQaoMau6INaHQFCbq1PhwIjgKv0Io')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Validate an address with address validation
# addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
#                                                     regionCode='US',
#                                                     locality='Mountain View', 
#                                                     enableUspsCass=True)

# COMMAND ----------

import requests
url = f'https://maps.googleapis.com/maps/api/geocode/json?place_id=ChIJeRpOeF67j4AR9ydy_PIzPuM&key={key}'
response = requests.get(url)

# COMMAND ----------


