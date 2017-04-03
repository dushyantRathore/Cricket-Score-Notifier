import notify2
import requests
import json
import pandas as pd
from prettytable import PrettyTable

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


url = "https://powerful-tor-13817.herokuapp.com/live"

headers = {
    'cache-control': "no-cache",
    'postman-token': "48cc4d45-5ce2-f04f-cc27-7f5b80874c59"
    }

response = requests.request("POST", url, headers=headers)
score = response.text
score = json.loads(score)
l = len(score["Matches"])

li = []

for i in range(0,l):
    li.append(score["Matches"][i]["Team A"] + " vs " + score["Matches"][i]["Team B"])

# print li

# Notification Tool

notify2.init("Cricket Notifier")
n = notify2.Notification("Live Scores", str(li))
n.show()

