import requests
class DataManager:
    def __init__(self):
        self.authorisation="Basic b3BpaWk6UmljaGFyZDE="
        self.header={
            "Authorization":self.authorisation
        }
        self.citycodes={"Paris":"PAR","Berlin":"BER","Tokyo":"TYO","Sydney":"SYD","Istanbul":"IST","Kuala Lumpur":"KUL","New York":"NYC","San Francisco":"SFO","Cape Town":"CPT"}
        self.Addtosheet()
    def Addtosheet(self):
        rownum=2
        for key in self.citycodes:
            params = {
                "price":{
                    "iataCode":self.citycodes[key]
                }
            }
            self.endpoint = "https://api.sheety.co/bc757108ae8348bdd9eb40e61eddd5d5/copyOfFlightDeals/prices/"+str(rownum)
            rownum+=1
            response=requests.put(url=self.endpoint,json=params,headers=self.header)
            print(response)
    def GetFromsheet(self):
        self.endpoint="https://api.sheety.co/bc757108ae8348bdd9eb40e61eddd5d5/copyOfFlightDeals/prices"
        response=requests.get(url=self.endpoint,headers=self.header)
        list=[]
        for row in response.json()["prices"]:
            info={
                "code":row["iataCode"],
                "price":row["lowestPrice"]
            }
            list.append(info)
            return list
            break


