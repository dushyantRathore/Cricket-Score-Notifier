import notify2
import requests
import json


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

    for i in range(0,l):
        result += str(score["Matches"][i]["Team A"]) + " vs " + str(score["Matches"][i]["Team B"] + "\n")

    # Notification Tool

    notify2.init("Cricket Notifier")
    n = notify2.Notification("Live Scores", result)
    n.show()

if __name__ == "__main__":
    getscore()

