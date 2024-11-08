import time
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

ORIGIN = 'MI'
DEPARTURE_TIME = datetime.now() + timedelta(days=1)



# pprint(data.sheet_data)
# Connect to Sheety
data = DataManager()

# Get cities with missing IATA codes
data.get_missing_iata()

# Connect to Flight Search
flight_s = FlightSearch()

# Get IATA codes for missing cities
for city, row_index in data.missing_iata_cities:
    time.sleep(1)
    iata = flight_s.get_iata(city)
    data.update_iata(iata, row_index)
data.get_sheety()

# create flight data objhects
flight_data = FlightData()

# get flight data based on our google sheets
for i in data.sheet_data['prices']:
    time.sleep(1)
    iata_code = i['iataCode']
    lowest_price = i['lowestPrice']
    row_number = i['id']
    city = i['city']
    # get all flight deals
    flight_deals = flight_s.get_flights(ORIGIN, iata_code, DEPARTURE_TIME)
    # finding if any flights are cheaper than usual
    flight_data.get_cheapest_flight(flight_deals)
    if flight_data.price < lowest_price:
        # update sheety price
        data.update_price(flight_data.price, row_number)
        # send notification
        print(f'Found lowest price for {city} at price {flight_data.price} USD on date {flight_data.departure_time}!')




