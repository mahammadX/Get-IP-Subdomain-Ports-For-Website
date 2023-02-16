#!/bin/bash
sleep 5
xdotool key Ctrl|xdotool key Shift|xdotool key N
sleep 5 
echo "=========>> Open My Page in GitHub "
xdotool type 'python3 openlinksinbrowser.py'
xdotool key Return
sleep 1
