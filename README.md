# NSBLive
BTCMonitor is a real-time Bitcoin price indicator for Linux operating systems (tested on Ubuntu 16.04). The price ticker updates every minute by default (this can be customized), and alerts you with a desktop notification if the Bitcoin price rises above or falls below a certain amount. I might expand the indicator and implement other cryptocurrencies in the future.

NSBLive 

## Preview:
![](https://i.imgur.com/4fp3rJZ.png)

## Installation:
Install all the Python3 dependencies:
```
$ sudo apt update && sudo apt upgrade
$ git clone https://github.com/sirajuddin97/BTCMonitor
[List is not complete! I'll add more dependencies later.]
```

## Run:
```
$ cd BTCMonitor
$ make
```

## Configuration:
There are three settings in the configuration file (*config.ini*), where **refresh_rate** is the amount of delay in seconds between each price lookup, **min_value** is the minimum price amount and **max_value** is the maximum price amount in order to trigger the desktop notification alert. These values are measured in USD.
```
[settings]
refresh_rate = 60
min_value = 8000
max_value = 10000
```
