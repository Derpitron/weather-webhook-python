import time
import requests
from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/864098878671814666/Kwu2gG373bBfWIR8t40cWb36bQgKdwHr9C-YfgnqYAVIiJHT9b_CKfEbfbgjfsV4yvE2")
url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'

while True:
	res = requests.get(url)
	data = res.json()
	weatherID = data['weather'][0]['id']
	cloud = data['clouds']['all']
	validWeather = ["200","201","202","210","211","212","221","230","231","232","300","301","302","310","311","312","313","314","321","503","504","511","520","521","522","530"]

	def rainCheck():
		if weatherID in validWeather:
			hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")

	def send():
		rainCheck()
		time.sleep(1200)
		
	send()
	#Cloud Cover
	if ((cloud >= 85) and (cloud <= 100)):
		print("DARKNESS RISES")

	time.sleep(300)