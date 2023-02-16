#!/bin/bash

xdotool key Ctrl|xdotool key Shift|xdotool key N
#sleep 5
echo "=========>> Scanning Website IP Address and Subdomain "
sleep 7
xdotool type 'python3 Getipandsubdomain.py'
 
xdotool key Return
sleep 1 

