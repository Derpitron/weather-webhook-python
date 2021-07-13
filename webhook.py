import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
api_url = os.getenv('API')
hook = Webhook(os.getenv('HOOK'))
x = 0

while True:
	response = requests.get(api_url)
	data = response.json()
	isRaining = data['rain']
	cloud1 = data['clouds']['all']

	if x == 0:
		isRaining2 = isRaining

	def rainCheck():
		if (("rain" in data) and (isRaining != isRaining2)):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")

	def cloudCheck():
			if (((cloud1 >= 85) and (cloud1 <= 100)) and ("rain" in isRaining == False)):
				hook.send("DARKNESS RISES")

	def send():
		rainCheck()
		cloudCheck()

	hook.send("rain" in isRaining)

	send()
	x += 1
	time.sleep(300)