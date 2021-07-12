import time
import requests
from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/864098878671814666/Kwu2gG373bBfWIR8t40cWb36bQgKdwHr9C-YfgnqYAVIiJHT9b_CKfEbfbgjfsV4yvE2")
url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'

while True:
	res = requests.get(url)
	data = res.json()
	weatherID1 = data['weather'][0]['id']
	weatherID2 = 0
	cloud = data['clouds']['all']
	validWeather = ["200","201","202","210","211","212","221","2"]

	def arive():
		hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
	
	def rainCheck():
		#Thunderstorm
		if (weatherID1 == 200):
			arive()
		elif (weatherID1 == 201):
			arive()
		elif (weatherID1 == 202):
			arive()
		elif (weatherID1 == 210):
			arive()
		elif (weatherID1 == 211):
			arive()
		elif (weatherID1 == 212):
			arive()
		elif (weatherID1 == 221):
			arive()
		elif (weatherID1 == 230):
			arive()
		elif (weatherID1 == 231):
			arive()
		elif (weatherID1 == 232):
			arive()

		#Drizzle
		elif (weatherID1 == 300):
			arive()
		elif (weatherID1 == 301):
			arive()
		elif (weatherID1 == 302):
			arive()
		elif (weatherID1 == 310):
			arive()
		elif (weatherID1 == 311):
			arive()
		elif (weatherID1 == 312):
			arive()
		elif (weatherID1 == 313):
			arive()
		elif (weatherID1 == 314):
			arive()
		elif (weatherID1 == 321):
			arive()

		#Rain
		elif (weatherID1 == 503):
			arive()
		elif (weatherID1 == 504):
			arive()
		elif (weatherID1 == 511):
			arive()
		elif (weatherID1 == 520):
			arive()
		elif (weatherID1 == 521):
			arive()
		elif (weatherID1 == 522):
			arive()
		elif (weatherID1 == 531):
			arive()

	def send():
		if (weatherID1 != weatherID2):
			rainCheck()

		time.sleep(1200)
		
	send()
	#Cloud Cover
	if ((cloud >= 85) and (cloud <= 100)):
		print("DARKNESS RISES")

	time.sleep(300)
	weatherID2 = weatherID1