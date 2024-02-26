#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint
import json

data_manager = DataManager()
fligh_data = FlightSearch()

sheet_data = data_manager.get_data_from_sheet()
#pprint(sheet_data)

if len(sheet_data[0]["iataCode"]) == 0:
    for element in sheet_data:
        element["iataCode"] = fligh_data.set_iata_code(element["city"])
    data_manager.dest_data = sheet_data
    data_manager.set_iata_codes_in_sheety()

search_result = []
for element in sheet_data:
    city = element["iataCode"]
    search_result.append(fligh_data.serch_for_flights(city))

for i in range(len(sheet_data)):
    if search_result[i]["price"] != None and (search_result[i]["price"] < sheet_data[i]["lowestPrice"]):
        print(True)


"""with open("flight_data.json", mode="w") as file:
    json.dump(flight, file)"""