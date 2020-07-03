import os
import requests
from colorama import Fore, Back, Style

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

os.system("cls")

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
usernames = os.path.join(ROOT_PATH, "usernames.txt")
result = os.path.join(ROOT_PATH, "results.txt")

# 404 - invalid
# 200 - valid

url = "https://soundcloud.com/"

a = open(usernames,"r").readlines()
file = [s.rstrip()for s in a]

for lines in file:

	username = lines.split()[0]

	done = url+username

	r = requests.get(done)

	if r.status_code == 404:
		print(green+username,"| Available")
		with open(result,"a") as work:
			work.write(username+"\n")
	elif r.status_code == 200:
		print(red+username,"| Unavailable")