import os, signal, gi, webbrowser, urllib.request, json, time, subprocess as s
gi.require_version('Gtk', '3.0');
gi.require_version('AppIndicator3', '0.1');
from gi.repository import Gtk, AppIndicator3, GObject
from threading import Thread
from configparser import ConfigParser
from dateutil import parser
from translate import *

class Indicator():
    def __init__(self):
        self.app = 'show_proc';
        config = ConfigParser();
        config.read('config.ini');
        self.language = config.get('settings', 'language');
        self.refresh_rate = config.getint('settings', 'refresh_rate');
        self.station = config.getint('settings', 'station_id');

        currpath = os.path.dirname(os.path.realpath(__file__));
        self.icon_small = currpath + '/img/nsb_small.png';
        self.icon_large = currpath + '/img/nsb_large.png';

        self.ind = AppIndicator3.Indicator.new(self.app, self.icon_small, AppIndicator3.IndicatorCategory.OTHER);
        self.ind.set_label(('NSB (%s)' % self.getStation()), self.app);
        self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE);
        self.ind.set_menu(self.create_menu());

        self.update = Thread(target = self.refreshPrice);
        self.update.setDaemon(True);
        self.update.start();

    def create_menu(self):
        menu = Gtk.Menu();
        submenu = Gtk.Menu();

        item_departures = Gtk.MenuItem(translate("departures", self.language));
        item_departures.set_submenu(submenu);
        menu.append(item_departures);

        for i in range(0, self.getTrainAmount()):
            submenu.append(Gtk.MenuItem(self.trainInfo()));

        item_separator = Gtk.SeparatorMenuItem();
        menu.append(item_separator);

        item_settings = Gtk.MenuItem(translate("settings", self.language));
        item_settings.connect('activate', self.settings);
        menu.append(item_settings);

        item_git = Gtk.MenuItem(translate("open", self.language));
        item_git.connect('activate', self.github);
        menu.append(item_git);

        item_quit = Gtk.MenuItem(translate("quit", self.language));
        item_quit.connect('activate', self.stop);
        menu.append(item_quit);

        menu.show_all();
        return menu;

    def getTrainAmount(self):
        api = ('http://reisapi.ruter.no/StopVisit/GetDepartures/%i?transporttypes=Train&callback=?' % self.station);

        with urllib.request.urlopen(api) as url:
            api = url.read().decode();
            api = api.replace('(', '');
            api = api.replace(')', '');
            api = api.replace('?', '');
            api = api.replace(';', '');
            data = json.loads(api);
            return len(data);

    def trainInfo(self):
        api = ('http://reisapi.ruter.no/StopVisit/GetDepartures/%i?transporttypes=Train&callback=?' % self.station);

        with urllib.request.urlopen(api) as url:
            api = url.read().decode();
            api = api.replace('(', '');
            api = api.replace(')', '');
            api = api.replace('?', '');
            api = api.replace(';', '');
            data = json.loads(api);
            data_size = len(data);

            for i in range(0, data_size):
                destination_name = data[i]['MonitoredVehicleJourney']['DestinationName'];
                platform = data[i]['MonitoredVehicleJourney']['MonitoredCall']['DeparturePlatformName'];
                departure_time = data[i]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime'];
                dt = parser.parse(departure_time);
                dt = "{}:{}".format(dt.hour, dt.minute);
                return ("%s til %s - %s (Spor %s)" % (self.getStation(), destination_name, dt, platform));

    def getStation(self):
        api = ('http://reisapi.ruter.no/Place/GetStop/%i?callback=?' % self.station);

        with urllib.request.urlopen(api) as url:
            api = url.read().decode();
            api = api.replace('(', '');
            api = api.replace(')', '');
            api = api.replace('?', '');
            api = api.replace(';', '');
            data = json.loads(api);
            district = data['District'];
            return district;

    def refreshPrice(self):
        while True:
            time.sleep(self.refresh_rate);
            GObject.idle_add(self.ind.set_label, self.getStation(), self.app, priority = GObject.PRIORITY_DEFAULT);

    def priceAlert(self, price):
        minAlert = 9000;
        maxAlert = 11000;

        if(maxAlert <= price):
            s.call(['notify-send', '-i', self.icon_large, 'NSBAlert', ('Hurray! Bitcoin price has reached $%s.' % round(price))]);
        elif(minAlert >= price):
            s.call(['notify-send', '-i', self.icon_large, 'NSBAlert', ('Oh no! Bitcoin price has dropped to $%s.' % round(price))]);

    def settings(self, source):
        os.system('xdg-open config.ini')

    def github(self, source):
        webbrowser.open('https://github.com/sirajuddin97/NSBAlert');

    def stop(self, source):
        Gtk.main_quit();

Indicator();
GObject.threads_init();
signal.signal(signal.SIGINT, signal.SIG_DFL);
Gtk.main();
