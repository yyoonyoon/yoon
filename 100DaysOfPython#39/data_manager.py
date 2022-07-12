import requests

sheety_endpoint = "https://api.sheety.co/20fce46d19b1ad0f507c96f99d704f10/flightDeals/prices"
iata_codes = ["PAR","BER","TYO","SYO","IST","KUL","NYC","SFO","SEL"]
k = 0

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url= sheety_endpoint)
        data = response.json()
        destination_data = data["prices"]

    def add_destination_code(self):
        global k
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": iata_codes[k]
                }
            }
            k += 1
            response = requests.put(url= f"{sheety_endpoint}/{city['id']}", json= new_data)