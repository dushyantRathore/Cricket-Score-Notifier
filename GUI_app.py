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
    print x
    l1 = len(x["Matches"])
    y = get_news()
    print y
    l2 = len(y["Latest News"])

    score = gtk.MenuItem("Live Score")
    news = gtk.MenuItem("Latest News")
    exit = gtk.MenuItem("Exit")
    exit.connect('activate', stop)
    sep = gtk.SeparatorMenuItem()

    score_submenu = gtk.Menu()
    for i in range(0, l1):
        r = ' '
        r += "Teams - " + str(x["Matches"][i]["Team A"]) + " v/s " + str(x["Matches"][i]["Team B"]) + "\n"
        r += "Status - " + x["Matches"][i]["Status"].encode('utf-8').strip()
        score_submenu.append(gtk.MenuItem(r))
        score_submenu.append(gtk.SeparatorMenuItem())

    score.set_submenu(score_submenu)

    news_submenu = gtk.Menu()
    for j in range(0, l2):
        r = ' '
        r += str(y["Latest News"][j]["Title"])
        news_submenu.append(gtk.MenuItem(r))
        news_submenu.append(gtk.SeparatorMenuItem())

    news.set_submenu(news_submenu)

    main_menu.append(score)
    main_menu.append(sep)
    main_menu.append(news)
    main_menu.append(sep)
    main_menu.append(exit)

    main_menu.show_all()
    return main_menu


def get_score():
    url = "https://powerful-tor-13817.herokuapp.com/live"
    response = requests.get(url)
    response = json.loads(response.text)

    return response


def get_news():
    url = "https://powerful-tor-13817.herokuapp.com/news"
    response = requests.get(url)
    response = json.loads(response.text)

    return response


def stop(self):
    gtk.main_quit()


if __name__ == "__main__":
    main()