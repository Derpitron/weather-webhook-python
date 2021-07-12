from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/863990102765207592/h8xfhL2ksmp-u-YI3uySYTwSUcV0cfezexbcjLNlytk9srp6hnnz3ZFbyyhaoSC1vbZk")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']

if weatherid == 500:
    hook.send(weatherid)
