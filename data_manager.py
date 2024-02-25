from dotenv import load_dotenv
import os
import requests

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = f"Bearer {os.getenv("SHEETY_TOKEN")}"

SHEETY_HEADER = {
    "Authorization": SHEETY_TOKEN
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.dest_data = []

    def get_data_from_sheet(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        response.raise_for_status()
        data = response.json()
        self.dest_data = data["prices"]
        return self.dest_data



    def set_iata_codes_in_sheety(self):
        for city in self.dest_data:
            params = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{city["id"]}", json=params, headers=SHEETY_HEADER)