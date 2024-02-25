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
    def __init__(self):
        self.iata_code = ""

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