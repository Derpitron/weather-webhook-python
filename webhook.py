from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/863990102765207592/h8xfhL2ksmp-u-YI3uySYTwSUcV0cfezexbcjLNlytk9srp6hnnz3ZFbyyhaoSC1vbZk")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']

if weatherid != 500:
    hook.send(weatherid)
if weatherid != 600:
    hook.send(weatherid)
if weatherid != 600:
    hook.send(weatherid)
if weatherid != 601:
    hook.send(weatherid)
if weatherid != 602:
    hook.send(weatherid)
if weatherid != 611:
    hook.send(weatherid)
if weatherid != 612:
    hook.send(weatherid)
if weatherid != 613:
    hook.send(weatherid)
if weatherid != 615:
    hook.send(weatherid)
if weatherid != 616:
    hook.send(weatherid)
if weatherid != 620:
    hook.send(weatherid)
if weatherid != 621:
    hook.send(weatherid)
if weatherid != 622:
    hook.send(weatherid)
if weatherid != 701:
    hook.send(weatherid)
if weatherid != 711:
    hook.send(weatherid)
if weatherid != 721:
    hook.send(weatherid)
if weatherid != 731:
    hook.send(weatherid)
if weatherid != 741:
    hook.send(weatherid)
if weatherid != 751:
    hook.send(weatherid)
if weatherid != 761:
    hook.send(weatherid)
if weatherid != 771:
    hook.send(weatherid)
if weatherid != 781:
    hook.send(weatherid)
if weatherid != 801:
    hook.send(weatherid)
if weatherid != 802:
    hook.send(weatherid)
if weatherid != 803:
    hook.send(weatherid)
if weatherid != 804:
    hook.send(weatherid)