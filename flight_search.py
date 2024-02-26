import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

KIWI_ENDPOINT = os.getenv("KIWI_ENDPOINT")
FLIGHT_KEY = os.getenv("FLIGHT_KEY")

HEADER = {
    "apikey": FLIGHT_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
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
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
        search_data = {
            "fly_from": "BUD",
            "fly_to": city_code,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_month_from_today.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "curr": "HUF",
            "max_stopovers": 2
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}v2/search", params=search_data, headers=HEADER)
        data = response.json()["data"]
        if len(data) > 0:
            flight = {
                "destination": city_code,
                "departure": data[0]["local_departure"].split("T")[0],
                "nights": data[0]["nightsInDest"],
                "price": data[0]["price"]
            }
        else:
            flight = {
                "destination": city_code,
                "departure": None,
                "nights": None,
                "price": None
            }
        return flight