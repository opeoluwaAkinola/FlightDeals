#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import json

manage=DataManager()
places_to_visit=manage.GetFromsheet()

flightsearch=FlightSearch("DUB",places_to_visit,"01/08/2022","05/08/2022")
searchresults=flightsearch.findflight()

flightdata=FlightData(searchresults,places_to_visit)
list_of_cheapest=flightdata.getCheapest()

notify=NotificationManager(list_of_cheapest,"01/08/2022","05/08/2022")
print(notify.sendMessage())
# with open("data.json","w") as file:
#     data=json.dumps(result.findflight(),indent=4)
#     file.write(data)

print(list_of_cheapest)