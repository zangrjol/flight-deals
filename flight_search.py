import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.url_iata = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
        self.url_offers = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._secret_key = os.getenv("AMADEUS_API_SECRET")
        self._access_token = self.get_bearer_token()  # os.getenv("AMADEUS_access_token")

    def get_bearer_token(self):
        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',

        }
        body = {
            'grant_type': "client_credentials",
            'client_id': self._api_key,
            'client_secret': self._secret_key,
        }
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        access_token = response.json()['access_token']
        return access_token

    def get_iata(self, city):
        headers = {
            'Authorization': f'Bearer {self._access_token}'
        }
        parameters = {
            'keyword': city.upper(),
            'max': 1
        }

        response = requests.get(self.url_iata, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        iata = data['data'][0]['iataCode']
        return iata

    def get_flights(self, origin_city_code, destination_city_code, from_time):
        headers = {
            'Authorization': f'Bearer {self._access_token}'
        }
        parameters = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            # "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(self.url_offers, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data


