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

team_A = []
team_B = []

for i in range(0,l):
    team_A.append(score["Matches"][i]["Team A"])
    team_B.append(score["Matches"][i]["Team B"])

sequence = ["Index", "Team A", "Team B"]

print color.GREEN + color.BOLD + color.UNDERLINE + str("The following matches are being played currently : ") + color.END
print "\n"

t = PrettyTable(sequence)

for i in range(0, len(team_A)):
    t.add_row([str(i+1), team_A[i], team_B[i]])

print t

final_list = []
for i,j in zip(team_A, team_B):
    final_list.append(str(i) + " vs " + str(j))

choice = int(raw_input(color.RED + color.BOLD + "\nEnter your choice : " + color.END))

# Notification Tool

notify2.init("Cricket Notifier")
n = notify2.Notification("Live Scores", str(final_list[choice - 1]))
n.show()

