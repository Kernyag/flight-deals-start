import requests
from dotenv import load_dotenv
import os

load_dotenv()

KIWI_ENDPOINT = os.getenv("KIWI_ENDPOINT")
FLIGHT_KEY = os.getenv("FLIGHT_KEY")

HEADER = {
    "apikey": FLIGHT_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def set_iata_code(self, city_name):
        parameters = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}locations/query", params=parameters, headers=HEADER)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
    
    def serch_for_flights(self, city_code):
        search_data = {
            "fly_from": "BUD",
            "fly_to": city_code,
            "date_from": "26/02/2024",
            "date_to": "30/03/2024",
            "max_stopovers": 1
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}search", params=search_data, headers=HEADER)
        flights = response.json()
        return flights