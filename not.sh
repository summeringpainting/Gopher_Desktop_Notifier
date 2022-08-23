#!/bin/bash
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" && notify-send "Gopher" "<a href=\"https://gopher.floodgap.com/gopher/gw?=gopher.club+70+312f70686c6f67732f\">NEW_PHLOGS</a>" && rm /home/steve/Python/gopherscraper/phlogs1.csv && cp /home/steve/Python/gopherscraper/phlogs.csv /home/steve/Python/gopherscraper/phlogs1.csv
