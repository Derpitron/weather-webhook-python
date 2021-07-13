import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
api_url = os.getenv('API')
hook = Webhook(os.getenv('HOOK'))

while True:
	res = requests.get(api_url)
	data = res.json()
	weatherID1 = data['weather'][0]['id']
	cloud1 = data['clouds']['all']
	validWeather = ["200","201","202","210","211","212","221","230","231","232","300","301","302","310","311","312","313","314","321","503","504","511","520","521","522","530"]

	def rainCheck():
		if (weatherID1 in validWeather) and (weatherID2 in validWeather == 0):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")

	def cloudCheck():
    		if (((cloud1 >= 85) and (cloud1 <= 100)) and (weatherID1 in validWeather == 0) and ((cloud2 < 85))):
    			hook.send("DARKNESS RISES")	

	def send():
		rainCheck()
		cloudCheck()
	
	hook.send(weatherID1)
		
	send()
	time.sleep(300)
	weatherID2 = weatherID1
	cloud2 = cloud1