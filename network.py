import requests
from payload import *
from error_codes import NO_DATA
from payload_types import MERO_LAGANI
import time
import random

class NetworkRequest:
    # def __init__(self, date, payload):
        

    def fetch_data(self, date: str, payload_type):
        if payload_type == MERO_LAGANI:
            #Adding a random delay to throwoff the scrap filters
            delay = random.randint(1, 4)
            time.sleep(delay)

            url = "https://merolagani.com/StockQuote.aspx"


            payload = get_mero_lagani_payaload(date)
        
            headers = {
            'Cookie': 'ASP.NET_SessionId=2ucimswv2t5m3sr3yb5df2t1'
            }
            return self.get_data(url, payload, headers)

    def get_data(self,url, payload, headers):
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        if response.status_code == 200:
            print(response.status_code)
            return response.text
        else:
            return NO_DATA