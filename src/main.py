import time
from datetime import datetime as dt

host_temp = r"DATA\Hosts\hosts"
host_path = r"C:\Windows\System32|drivers\etc\hosts"
redirect = "127.0.0.1"
site_lst = ["www.facebook.com", "facebook.com", "www.nerdmafia.com", "nerdmafia.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working...")
		with open(host_temp, "r+") as file:
			content = file.read()
			for website in site_lst:
				if website in content:
					pass
				else:
					file.write("\n" + redirect + " " + website + "\n")
	else:
		print("off hours...")
		with open(host_temp, "r+") as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in site_lst):
					file.write(line)
			file.truncate()
	time.sleep(5)
