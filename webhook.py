from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/864019084655853579/N1BAd9yGDmRg0Jk7UFyGl2y41cQTsHsjem8N-Hw3_31MxyCP678GkMiCN7CqL1suuPtM")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']
cloud = data['weather']['clouds']['all']

#Thunderstorm
if (weatherid == 200):
    hook.send("THE CLOUD HAS ARIVED")
elif (weatherid == 201):
    hook.send("THE CLOUD HAS ARIVED2")
elif (weatherid == 202):
    hook.send("THE CLOUD HAS ARIVED3")
elif (weatherid == 210):
    hook.send("THE CLOUD HAS ARIVED4")
elif (weatherid == 211):
    hook.send("THE CLOUD HAS ARIVED5")
elif (weatherid == 212):
    hook.send("THE CLOUD HAS ARIVED6")
elif (weatherid == 221):
    hook.send("THE CLOUD HAS ARIVED7")
elif (weatherid == 230):
    hook.send("THE CLOUD HAS ARIVED8")
elif (weatherid == 231):
    hook.send("THE CLOUD HAS ARIVED9")
elif (weatherid == 232):
    hook.send("THE CLOUD HAS ARIVED10")

#Drizzle
elif (weatherid == 300):
    hook.send("THE CLOUD HAS ARIVED11")
elif (weatherid == 301):
    hook.send("THE CLOUD HAS ARIVED12")
elif (weatherid == 302):
    hook.send("THE CLOUD HAS ARIVED13")
elif (weatherid == 310):
    hook.send("THE CLOUD HAS ARIVED14")
elif (weatherid == 311):
    hook.send("THE CLOUD HAS ARIVED15")
elif (weatherid == 312):
    hook.send("THE CLOUD HAS ARIVED16")
elif (weatherid == 313):
    hook.send("THE CLOUD HAS ARIVED17")
elif (weatherid == 314):
    hook.send("THE CLOUD HAS ARIVED18")
elif (weatherid == 321):
    hook.send("THE CLOUD HAS ARIVED19")

#Rain
elif (weatherid == 502):
    hook.send("THE CLOUD HAS ARIVED20")
elif (weatherid == 503):
    hook.send("THE CLOUD HAS ARIVED21")
elif (weatherid == 504):
    hook.send("THE CLOUD HAS ARIVED22")
elif (weatherid == 511):
    hook.send("THE CLOUD HAS ARIVED23")
elif (weatherid == 520):
    hook.send("THE CLOUD HAS ARIVED24")
elif (weatherid == 521):
    hook.send("THE CLOUD HAS ARIVED25")
elif (weatherid == 522):
    hook.send("THE CLOUD HAS ARIVED26")
elif (weatherid == 531):
    hook.send("THE CLOUD HAS ARIVED27")
else:
    hook.send("no cloud")

#Cloud Cover
if (((cloud >= 70) and (cloud <= 100)) and ((weatherid == 500) or (weatherid == 501))):
    hook.send("The cloud may be ariving")