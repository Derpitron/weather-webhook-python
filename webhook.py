from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/864019084655853579/N1BAd9yGDmRg0Jk7UFyGl2y41cQTsHsjem8N-Hw3_31MxyCP678GkMiCN7CqL1suuPtM")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']

if weatherid != 500:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 600:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 600:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 601:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 602:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 611:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 612:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 613:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 615:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 616:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 620:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 621:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 622:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 701:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 711:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 721:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 731:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 741:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 751:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 761:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 771:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 781:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 801:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 802:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 803:
    hook.send("THE CLOUD HAS ARIVED")
elif weatherid != 804:
    hook.send("THE CLOUD HAS ARIVED")
