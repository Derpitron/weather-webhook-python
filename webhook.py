import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
x = 0
while True:
	response = requests.get(os.getenv('API'))
	data = response.json()
	rainData = data['rain']
	isRaining = "rain" in rainData
	if x == 0:
		isRaining2 = False
	def rainCheck():
		if ((isRaining) and (isRaining != isRaining2)):
			Webhook(os.getenv('HOOK')).send("THE CLOUD HAS ARIVED")
			Webhook(os.getenv('HOOK')).send("JJJJJJJJJJJJJJJJ")
	def send():
		rainCheck()
	isRaining2 = isRaining
	send()
	x += 1
	time.sleep(300)