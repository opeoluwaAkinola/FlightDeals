import requests

class FlightSearch:
    def __init__(self,flyFrom,flyTo,dateFrom,dateTo):
        self.APIKEY="1dpudZ_0Jw2qhBqjSQ_1J-hTizoUfhxW"
        self.ENDPOint="https://tequila-api.kiwi.com/v2/search"
        self.flyfrom=flyFrom
        self.places=flyTo
        self.datefrom=dateFrom
        self.dateto=dateTo
        self.headers={
            "Content-Type": "application / json",
            "Content-Encoding": "gzip",
            "apikey":self.APIKEY
        }
    def findflight(self):
        list={}
        for place in self.places:
            self.parameters = {
                "fly_from": self.flyfrom,
                "fly_to": place["code"],
                "date_From": self.datefrom,
                "date_to": self.dateto
            }
            try:
                response=requests.get(url=self.ENDPOint,params=self.parameters,headers=self.headers)
            except requests.exceptions:
                values=None

            else:
                values=response.json()
            list[place["code"]]=values
        return list

