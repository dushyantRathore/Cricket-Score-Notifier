import os
import signal
import gi

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
    item1 = gtk.MenuItem("Score")
    item2 = gtk.SeparatorMenuItem()
    item3 = gtk.MenuItem("Exit")

    main_menu.append(item1)
    main_menu.append(item2)
    main_menu.append(item3)

    main_menu.show_all()
    return main_menu

if __name__ == "__main__":
    main()