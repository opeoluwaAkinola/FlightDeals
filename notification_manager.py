from twilio.rest import Client

class NotificationManager:
    def __init__(self,lists,date_from,date_to):
        self.account_sid = 'AC13241ada11a9e19d5d169cc31b79eb44'
        self.auth_token = 'd2ff082edf8ba7ae260b0771f95bc5d2'
        self.lists=lists
        self.dateTo=date_to
        self.dateFrom=date_from

    def sendMessage(self):
        client = Client(self.account_sid, self.auth_token)
        for list in self.lists:
            if list["stop_overs"]>0:
                body=f"Lower price Alert! Only €{list['price']} to fly from {list['City from']}-{list['City from code']} to {list['City to']}-{list['City to code']} from {self.dateFrom} to {self.dateTo}\nFlight has {list['stop_overs']},via {list['via_city']}."
            else:
                body=f"Lower price Alert! Only €{list['price']} to fly from {list['City from']}-{list['City from code']} to {list['City to']}-{list['City to code']} from {self.dateFrom} to {self.dateTo}"
            message = client.messages.create(
                body=body,
                from_='+13202458736',
                to='+353892362724'
            )
            return message.status