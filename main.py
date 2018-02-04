import os, signal, gi, webbrowser, urllib.request, json, time, subprocess as s
gi.require_version('Gtk', '3.0');
gi.require_version('AppIndicator3', '0.1');
from gi.repository import Gtk, AppIndicator3, GObject
from threading import Thread

class Indicator():
    def __init__(self):
        self.app = 'show_proc';
        self.currpath = os.path.dirname(os.path.realpath(__file__));
        iconpath = self.currpath + '/img/nsb_small.png';

        self.ind = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER);
        self.ind.set_label('NSB (Drammen)', self.app);
        self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE);
        self.ind.set_menu(self.create_menu());

        self.update = Thread(target = self.refreshPrice);
        self.update.setDaemon(True);
        self.update.start();

    def create_menu(self):
        menu = Gtk.Menu();

        item_git = Gtk.MenuItem('Open GitHub');
        item_git.connect('activate', self.github);

        item_quit = Gtk.MenuItem('Quit');
        item_quit.connect('activate', self.stop);

        menu.append(item_git);
        menu.append(item_quit);
        menu.show_all();
        return menu;

    def price(self):
        api = 'https://blockchain.info/ticker';
        with urllib.request.urlopen(api) as url:
            data = json.loads(url.read().decode());
            btc_usd = data['USD']['last'];
            self.priceAlert(btc_usd);
            label = 'BTC: $' + str(round(btc_usd));
            return label;

    def refreshPrice(self):
        while True:
            time.sleep(5);
            GObject.idle_add(self.ind.set_label, self.price(), self.app, priority = GObject.PRIORITY_DEFAULT);

    def priceAlert(self, price):
        iconpath = self.currpath + '/img/nsb_large.png';
        minAlert = 9000;
        maxAlert = 11000;

        if(maxAlert <= price):
            s.call(['notify-send', '-i', iconpath, 'Bitcoin Price Indicator', ('Hurray! Bitcoin price has reached $%s.' % round(price))]);
        elif(minAlert >= price):
            s.call(['notify-send', '-i', iconpath, 'Bitcoin Price Indicator', ('Oh no! Bitcoin price has dropped to $%s.' % round(price))]);

    def github(self, source):
        webbrowser.open('https://github.com/sirajuddin97/NSBAlert');

    def stop(self, source):
        Gtk.main_quit();

Indicator();
GObject.threads_init();
signal.signal(signal.SIGINT, signal.SIG_DFL);
Gtk.main();
