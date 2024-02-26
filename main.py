#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os
from pprint import pprint
import json

load_dotenv()
EMAIL_PASSW = os.getenv("EMAIL_PASSW")

data_manager = DataManager()
fligh_data = FlightSearch()

sheet_data = data_manager.get_data_from_sheet() # Get data from the google sheet

# TODO Check if a new line was edded to the sheet and get the IATA code automaticly.
if len(sheet_data[0]["iataCode"]) == 0:
    for element in sheet_data:
        element["iataCode"] = fligh_data.get_iata_code(element["city"])
    data_manager.dest_data = sheet_data
    data_manager.set_iata_codes_in_sheety()

# TODO extend serch for flight with more parameters to easily modife search
search_result = [] # Data from the search will be added here / Price, departure, city, nights
for element in sheet_data:
    city = element["iataCode"]
    search_result.append(fligh_data.serch_for_flights(city))

# Check price and send notification if price is lower compared to the price in the google sheet
for i in range(len(sheet_data)):
    if search_result[i]["price"] != None and (search_result[i]["price"] < sheet_data[i]["lowestPrice"]):
        message = f"""
        Budapest - BUD to {sheet_data[i]["city"]} - {sheet_data[i]["iataCode"]}
        Price: {search_result[i]["price"]} HUF 
        from {search_result[i]["departure"]} for {search_result[i]["nights"]} nights.
        """
        notification = NotificationManager(from_email="gyorkerny@gmail.com", from_passw=EMAIL_PASSW, to_email="kernyag@hotmail.com", send_message=message)
        notification.send_notification()


"""with open("flight_data.json", mode="w") as file:
    json.dump(flight, file)"""

# TODO Create a customer manager, to be able to register with more email addresses