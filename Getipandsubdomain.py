#!/usr/bin/env python3
import socket
import requests
Web = input("Write Website to Scanning :  ")
def get_ip(website):
    try:
        print("IP Address for "+Web+" is : ",socket.gethostbyname(website))
    except socket.gaierror:
        print("ip Address Not Found for "+Web)
get_ip(Web)
def domain_scanner(domain_name,sub_domnames):
	print('----URL after scanning subdomains----')

	for subdomain in sub_domnames:
		url = f"https://{subdomain}.{domain_name}"
		try:
			requests.get(url)
			print(f'[+] {url}')
		except requests.ConnectionError:
			pass

# main function
if __name__ == '__main__':
	with open('subdo.txt','r') as file:
		name = file.read()
		sub_dom = name.splitlines()

	domain_scanner(Web,sub_dom)

print("================>> Programmer By Eng.MahammadQassem")