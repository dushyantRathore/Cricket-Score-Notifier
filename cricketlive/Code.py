import notify2
import requests
import json
import time

class Colour:
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


def getscore():

    url = "https://powerful-tor-13817.herokuapp.com/live"

    headers = {
        'cache-control': "no-cache",
        'postman-token': "48cc4d45-5ce2-f04f-cc27-7f5b80874c59"
        }

    response = requests.request("POST", url, headers=headers)
    score = response.text
    score = json.loads(score)

    l = len(score["Matches"])

    result = ''

    if l > 5:
        for i in range(0, 5):
            result += str(i+1) + ") " + str(score["Matches"][i]["Team A"]) + " vs " + str(score["Matches"][i]["Team B"] + "\n")
    elif l < 5 and l != 0:
        for i in range(0, l):
            result += str(i+1) + ") " + str(score["Matches"][i]["Team A"]) + " vs " + str(score["Matches"][i]["Team B"] + "\n")
    else:
        result += "No matches being played currently"

    # Notification Tool

    icon_path = "/home/dushyant/Desktop/Github/Cricket-Score-Notifier/cricketlive/icon.jpg"

    notify2.init("Cricket Notifier")
    n = notify2.Notification("Live Scores", icon=icon_path)
    n.update("Live Scores", result)
    n.show()


if __name__ == "__main__":
    getscore()

