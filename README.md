# NSBLive
To be updated...

## Preview:
![](https://i.imgur.com/RijcZer.png)
![](https://i.imgur.com/XuQWiNd.png)

## Installation:
Install all the Python3 dependencies:
```
$ sudo apt update && sudo apt upgrade
$ git clone https://github.com/sirajuddin97/NSBLive
[List is not complete! I'll add more dependencies later.]
```

## Run:
```
$ cd NSBLive
$ make
```

## Configuration:
There are three settings in the configuration file (*config.ini*), where you can change the application language, refresh rate and your train station ID.

**Available languages:** norwegian, english (no/en)
**Refresh rate:** Amount of delay in seconds between each lookup
**Station ID:** 

```
[settings]
language = no
refresh_rate = 300
station_id = 6049104
```
