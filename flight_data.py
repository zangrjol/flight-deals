class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = float('inf')
        self.arrival_iata = None
        self.departure_time = None

    def get_cheapest_flight(self, data):
        for i in data['data']:
            price = float(i['price']['total'])
            if price < self.price:
                self.price = price
                self.departure_time = i['itineraries'][0]['segments'][0]['departure']['at']
                self.arrival_iata = i['itineraries'][0]['segments'][0]['arrival']['iataCode']



