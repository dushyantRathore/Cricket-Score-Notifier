import os
import signal
import gi
import requests
import json

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'


def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                           os.path.abspath('/home/dushyant/Desktop/Github/Cricket-Score-Notifier/cricketlive/icon.jpg'),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(score_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()


def score_menu():
    main_menu = gtk.Menu()

    x = get_score()
    l = len(x["Matches"])

    for i in range(0, l):
        r = ' '
        r += "Teams - " + str(x["Matches"][i]["Team A"]) + " v/s " + str(x["Matches"][i]["Team B"]) + "\n"
        r += "Status - " + x["Matches"][i]["Status"].encode('utf-8').strip()
        main_menu.append(gtk.MenuItem(r))
        main_menu.append(gtk.SeparatorMenuItem())

    main_menu.show_all()
    return main_menu


def get_score():
    url = "https://powerful-tor-13817.herokuapp.com/live"
    response = requests.get(url)
    response = json.loads(response.text)

    return response

if __name__ == "__main__":
    main()