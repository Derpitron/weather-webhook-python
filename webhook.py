import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
hook = Webhook(os.getenv('HOOK'))
x = False
while True:
	response = requests.get(os.getenv('API'))
	data = response.json()
	rainData = data['rain']
	isRaining = "rain" in rainData
	if x == False:
		isRaining2 = False
	def rainCheck():
		if ((isRaining) and (isRaining != isRaining2)):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")
	isRaining2 = isRaining
	rainCheck()
	print(x)
	x = True
	time.sleep(60)