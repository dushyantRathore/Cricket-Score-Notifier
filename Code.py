import notify2
import requests
import json
import pandas as pd
from prettytable import PrettyTable

url = "https://powerful-tor-13817.herokuapp.com/live"

headers = {
    'cache-control': "no-cache",
    'postman-token': "48cc4d45-5ce2-f04f-cc27-7f5b80874c59"
    }

response = requests.request("POST", url, headers=headers)
score = response.text
score = json.loads(score)
l = len(score["Matches"])

team_A = []
team_B = []

for i in range(0,l):
    team_A.append(score["Matches"][i]["Team A"])
    team_B.append(score["Matches"][i]["Team B"])

sequence = ["Team A", "Team B"]
# t = PrettyTable(sequence)
#
# for i in range(0, len(team_A)):
#     t.add_row([team_A[i], team_B[i]])
# print t

final_list = []
for i,j in zip(team_A, team_B):
    final_list.append(str(i) + " vs " + str(j))

# Notification Tool

notify2.init("Cricket Notifier")
n = notify2.Notification("Live Scores", str(final_list[0]) + "\n" + str(final_list[1]))
n.show()

