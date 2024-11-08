import requests
import os
from dotenv import load_dotenv

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.url = 'https://api.sheety.co/78777d56d6c7d2733f9e73a006463a90/flightDealsAz/prices'
        self._bearer = os.getenv('SHEETY_BEARER')
        self.sheet_data = None
        self.get_sheety()
        self.missing_iata_cities = []

    def get_sheety(self):
        headers = {"Authorization": f'Bearer {self._bearer}'}
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data
        print("Sheet data updated")

    def get_missing_iata(self):
        for i in self.sheet_data['prices']:
            if i['iataCode'] == '':
                self.missing_iata_cities.append((i['city'], i['id']))

    def update_iata(self, iata_code, row):
        headers = {"Authorization": f'Bearer {self._bearer}'}
        body = {
            'price': {'iataCode': iata_code}
            }
        response = requests.put(f'{self.url}/{row}', headers=headers, json=body)
        response.raise_for_status()
        print("Sheet iata updated")

    def update_price(self, price, row):
        headers = {"Authorization": f'Bearer {self._bearer}'}
        body = {
            'price': {'lowestPrice': price}
        }
        response = requests.put(f'{self.url}/{row}', headers=headers, json=body)
        response.raise_for_status()
        print("Sheet lowest price updated")

