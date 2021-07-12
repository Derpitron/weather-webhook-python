import os
os.system('pip install -r requirements.txt')

from dhooks import Webhook
import requests
hook = Webhook("https://discord.com/api/webhooks/864019084655853579/N1BAd9yGDmRg0Jk7UFyGl2y41cQTsHsjem8N-Hw3_31MxyCP678GkMiCN7CqL1suuPtM")

url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['description']
weatherid = data['weather'][0]['id']

if (weatherid != 500 or weatherid != 600 or weatherid != 601 or weatherid != 602 or weatherid != 611 or weatherid != 612 or weatherid != 613 or weatherid != 615 or weatherid != 616 or weatherid != 620 or weatherid != 621 or weatherid != 622 or weatherid != 701 or weatherid != 711 or weatherid != 721 or weatherid != 731 or weatherid != 741 or weatherid != 751 or weatherid != 761 or weatherid != 771 or weatherid != 781 or weatherid != 801 or weatherid != 802 or weatherid != 803 or weatherid != 804):
    hook.send("THE CLOUD HAS ARIVED")
