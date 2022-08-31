class FlightData:
    def __init__(self,flightData,places):
        self.data=flightData
        self.places=places
        self.info={
            "stop_overs":0,
            "via_city":""
        }
    def getCheapest(self):
        list=[]
        for key in self.data:
            for place in self.places:
                if key == place["code"]:
                    for flights in self.data[key]["data"]:
                        if flights["price"]<= place["price"]:
                            self.info["City from"]=flights["cityFrom"]
                            self.info["City from code"]=flights["cityCodeFrom"]
                            self.info["City to"]=flights["cityTo"]
                            self.info["City to code"]=flights["cityCodeTo"]
                            self.info["price"]=flights["price"]
                            list.append(self.info)
        return list

