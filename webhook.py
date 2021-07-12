from dhooks import Webhook
import requests
import time
hook = Webhook("https://discord.com/api/webhooks/863990102765207592/h8xfhL2ksmp-u-YI3uySYTwSUcV0cfezexbcjLNlytk9srp6hnnz3ZFbyyhaoSC1vbZk")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weatherid = data['weather'][0]['id']
cloud = data['clouds']['all']

i = 0
while i <= 1700:
    i += 1
    if i == 1700:
        i = 0

def arive():
    if i == 0:
        hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")

#Thunderstorm
if (weatherid == 200):
    arive()
elif (weatherid == 201):
    arive()
elif (weatherid == 202):
    arive()
elif (weatherid == 210):
    arive()
elif (weatherid == 211):
    arive()
elif (weatherid == 212):
    arive()
elif (weatherid == 221):
    arive()
elif (weatherid == 230):
    arive()
elif (weatherid == 231):
    arive()
elif (weatherid == 232):
    arive()

#Drizzle
elif (weatherid == 300):
    arive()
elif (weatherid == 301):
    arive()
elif (weatherid == 302):
    arive()
elif (weatherid == 310):
    arive()
elif (weatherid == 311):
    arive()
elif (weatherid == 312):
    arive()
elif (weatherid == 313):
    arive()
elif (weatherid == 314):
    arive()
elif (weatherid == 321):
    arive()

#Rain
#elif (weatherid == 502):
    #hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ20")
elif (weatherid == 503):
    arive()
elif (weatherid == 504):
    arive()
elif (weatherid == 511):
    arive()
elif (weatherid == 520):
    arive()
elif (weatherid == 521):
    arive()
elif (weatherid == 522):
    arive()
elif (weatherid == 531):
    arive()

#Cloud Cover
if ((cloud >= 70) and (cloud <= 89)):
    print("The cloud may be ariving - source: clouds")
if ((cloud >= 90) and (cloud <= 100)):
    print("DARKNESS RISES")
if ((weatherid == 500) or (weatherid == 501) or (weatherid == 502)):
    print("The cloud may be ariving - source: precipitation")