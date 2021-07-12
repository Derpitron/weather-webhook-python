from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/863990102765207592/h8xfhL2ksmp-u-YI3uySYTwSUcV0cfezexbcjLNlytk9srp6hnnz3ZFbyyhaoSC1vbZk")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']
cloud = data['clouds']['all']

#Thunderstorm
if (weatherid == 200):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 201):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 202):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 210):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 211):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 212):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 221):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 230):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 231):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 232):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")

#Drizzle
elif (weatherid == 300):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 301):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 302):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 310):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 311):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 312):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 313):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 314):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 321):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")

#Rain
#elif (weatherid == 502):
    #hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ20")
elif (weatherid == 503):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 504):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 511):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 520):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 521):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 522):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
elif (weatherid == 531):
    hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")

#Cloud Cover
if ((cloud >= 70) and (cloud <= 100)):
    print("The cloud may be ariving - source: clouds")
if ((weatherid == 500) or (weatherid == 501) or (weatherid == 502)):
    print("The cloud may be ariving - source: precipitation")