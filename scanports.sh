#!/bin/bash
echo "=========>> Scanning Website Ports "
sleep 3
echo "Write The Website to Scan Open Ports"
read port
nmap -sV $port
 
xdotool key Return
sleep 1 
