# NSBLive
To be updated.

## Preview:
![](https://i.imgur.com/RijcZer.png)
![](https://i.imgur.com/XuQWiNd.png)

## Configuration:
There are three settings in the configuration file (*config.ini*), where you can change the program language, refresh rate and your train station ID. You must restart the program every time you update the configuration file.
```
[settings]
language = no
refresh_rate = 300
station_id = 6049104
```
**Available languages:** You can choose between norwegian and english (no/en).

**Refresh rate:** Amount of delay in seconds between each lookup. 300 seconds (5 minutes) is recommended.

**Station ID:** Go to https://ruter.no/reiseplanlegger and enter your station information (departure/arrival). Click "Find journey" and copy your station ID from the URL (it looks something like this: .../reiseplanlegger/Mellom/Fra/**(6021000)**). Paste this ID in your configuration file and restart the program.
![](https://i.imgur.com/3SnsPtA.png)
![](https://i.imgur.com/xMyzeN7.png)

Let me know if you have any questions. Enjoy and good luck!