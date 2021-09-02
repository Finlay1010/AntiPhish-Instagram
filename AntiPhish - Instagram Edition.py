"""
AntiPhish: Instagram Edition - Destroying a continuous scam that has lasted too long
Copyright (C) 2021  Finlay1010

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import time
import random
import threading
import ctypes
import string
import json
import subprocess

def check_modules():
	print("Checking if all necessary modules are installed...")
	
	try:
		import requests
	except:
		print("[ERROR] - Module 'requests' not installed!\nTo install, open 'Command Prompt' and type 'pip install requests' and wait.")
		time.sleep(5)
		quit()

	print("Done!")
	time.sleep(0.1)

check_modules()
import requests

lock = threading.Lock()

proxy_list = []
user_agents = []
sent_count = 0
proxy_errors = 0
credits_message = 0

try:
	with open('user-agents.txt', 'r') as file:
		for UA in file:
			try:
				UA1 = UA.replace('\n', '')
				user_agents.append(UA1)
			except:
				pass
except FileNotFoundError:
	input("\n[ERROR] - 'user-agents.txt' file not found, you should have downloaded this file from my Github page with this program.\nYou can download it from: https://github.com/Finlay1010/AntiPhish-Instagram")
	quit()


def logo():
	os.system("cls")
	print('''\u001b[36;1m
 █████╗ ███╗   ██╗████████╗██╗██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗████╗  ██║╚══██╔══╝██║██╔══██╗██║  ██║██║██╔════╝██║  ██║
███████║██╔██╗ ██║   ██║   ██║██████╔╝███████║██║███████╗███████║
██╔══██║██║╚██╗██║   ██║   ██║██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║  ██║██║ ╚████║   ██║   ██║██║     ██║  ██║██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
--------------------- { INSTAGRAM EDITION } ---------------------
\u001b[0m''')

def credits():
	global credits_message
	
	while True:
		try:
			logo()
			print("THANKS TO:\n\nBuilt-in proxies provided by - https://proxyscrape.com\nUser-agents list provided by - https://user-agents.net\nRandom usernames provided by - https://namefake.com\n\n\n\nLiterally everything else by:")
			print('''\u001b[31;1m
███████ ██ ███    ██ ██       █████  ██    ██  ██  ██████   ██  ██████  
██      ██ ████   ██ ██      ██   ██  ██  ██  ███ ██  ████ ███ ██  ████ 
█████   ██ ██ ██  ██ ██      ███████   ████    ██ ██ ██ ██  ██ ██ ██ ██ 
██      ██ ██  ██ ██ ██      ██   ██    ██     ██ ████  ██  ██ ████  ██ 
██      ██ ██   ████ ███████ ██   ██    ██     ██  ██████   ██  ██████  ''')
		
			if credits_message == 0:
				print("------- { Send me Bitcoin? 1FinLayTxovShtRaPyaYc2oEdt88yVEWCz } -------")
				credits_message += 1
			elif credits_message == 1:
				print("--- { Send me Ethereum? 0xFCC4EaAee8c941B0821CfC0be34d77b7a664E7C1 } ---")
				credits_message += 1
			elif credits_message == 2:
				print("Send me any ERC20/BEP20 token? 0xFCC4EaAee8c941B0821CfC0be34d77b7a664E7C1")
				credits_message += 1
			elif credits_message == 3:
				print("Send me BNB or any BEP2 token? bnb1kggtrwd7ng0xe7rr7e20skzv96mx8pv3v29tjh")
				credits_message -= 3

			print("\u001b[0m\n\n\n\n(To return to the menu, press both 'Ctrl' and 'c' keys at the same time)")
			time.sleep(4)
	
		except KeyboardInterrupt:
			break

	menu()

def scrape_proxies():
	global proxy_list

	logo()

	try:
		proxyfile = open("proxies.txt", "x")
		proxyfile.close()
	except:
		pass

	ask_if_scrape = input("Do you already have a list of proxies that you want to use for this? (HTTP/HTTPS)\n[1] - Yes\n[2] - No\n\n")

	if ask_if_scrape == '1':
		input("\nOk! Simply paste your proxy list into the 'proxies.txt' file that you downloaded with this program, save it, then press the enter key.")
		os.system("cls")
	elif ask_if_scrape == '2':
		print("\nOk! Scraping proxies...")
		get_proxies = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=elite&simplified=true").text
		with open("proxies.txt", "w+") as file:
			file.write(get_proxies)
		print("Done!")
		time.sleep(0.5)
		os.system("cls")
	else:
		print("[ERROR] - INVALID INPUT: Enter the assigned number of the option that you want to choose.")
		time.sleep(2)
		os.system("cls")
		scrape_proxies()

	logo()

	with open("proxies.txt", "r+") as file:
		read = file.readlines()
		for lines in read:
			try:
				replace = lines.split()[0].replace('\n', '')
				proxy_list.append(replace)
			except:
				pass


def run(url):
	global proxy_list, proxy_errors, sent_count, user_agents

	random_proxy = random.choice(proxy_list)
	random_user_agent = random.choice(user_agents)

	proxy = {
	'http': random_proxy, 
	'https': random_proxy
	}

	try:
		req_username = requests.get("https://api.namefake.com/random/random", proxies=proxy, timeout=5).json()
		random_username = str(req_username["username"])

		full_url = url + random_username
		scam_url = requests.get(full_url, headers={"user-agent": str(random_user_agent)}, proxies=proxy, timeout=5).url

		if random.randrange(1,3) == 1:
			all_characters = string.ascii_letters + string.digits + string.punctuation
		else:
			all_characters = string.ascii_letters + string.digits
		
		random_password = "".join(random.sample(all_characters, random.randrange(6,40)))

		postdata = {
		'dim': '{"w":2560,"h":1440,"aw":2560,"ah":1400,"c":24}',
		'username': random_username,
		'password': random_password
		}

		post = requests.post(scam_url, data=postdata, headers={"user-agent": str(random_user_agent)}, proxies=proxy, timeout=5)

		if post.status_code == 200:
			sent_count += 1
		else:
			proxy_errors +=1
	
	except:
		proxy_errors += 1


def menu():
	ctypes.windll.kernel32.SetConsoleTitleW("AntiPhish: Instagram Edition - Coded by Finlay | Github.com/Finlay1010")
	logo()

	menu_option = input("Where would you like to go?\n\n[1] - Main Tool\n[2] - Credits\n\n")
	
	if menu_option == "1":
		pass
	elif menu_option == "2":
		credits()
	else:
		print("[ERROR] - INVALID INPUT: Enter the assigned number of the option that you want to choose.")
		time.sleep(2)
		menu()

	os.system("cls")
	input("Use of some features of this program may be illegal in your country.\n\nBy continuing you agree that the developer of this program will not be held responsible for any illegal activies that are committed by you (the user) via this program.")
	os.system("cls")
	input("It is recommended to use a VPN while using this program, ESPECIALLY if you're using free proxies / the proxies provied by the program, however it is NOT REQUIRED.")
	logo()
	url = input("Enter the scam link you were sent WITHOUT your username: ")
	scrape_proxies()

	while True:
		if threading.active_count() <= 200:
			try:
				threading.Thread(target = run, args = (url,)).start()
				ctypes.windll.kernel32.SetConsoleTitleW('AntiPhish: Instagram Edition - Coded by Finlay | Fake Passwords Sent: ' + str(sent_count) + ' | Proxy errors: ' + str(proxy_errors) + ' | Github.com/Finlay1010')
			except:
				pass


menu()
