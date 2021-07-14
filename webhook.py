import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
hook = Webhook(os.getenv('HOOK'))
x = 0
while True:
	response = requests.get(os.getenv('API'))
	data = response.json()
	rainData = data['rain']
	isRaining = "rain" in rainData
	if x == 0:
		isRaining2 = False
		if x >= 3:
			x = 1
	def rainCheck():
		if ((isRaining) and (isRaining != isRaining2)):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")
	isRaining2 = isRaining
	rainCheck()
	x += 1
	time.sleep(60)