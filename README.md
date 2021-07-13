# weather-webhook

This is a small project I made and fjsdkfhlkdsh im too lazy to write this readme.md
uhh

this is a script which pulls current weather from openweathermap and if it is raining, then it sends a message through discord webhook. it has a feature where it does not send the message until and unless the variable changes. this part took me much longer than i'd like to figure out.


clone the repository, cd into it, pip install -r requirements.txt

then in .env change the placeholders to your discord webhook link and openweather api link (note: this script was built with the OpenWeatherMap Current Weather API in mind so dont use any other API. also use latitude and longitude of your location, or it's openweathermap ID, or ISO 3166 compliant name. remember to put your API key as well or else you'll get error 401 (invalid authentication).

now run webhook.py. if you want to change the interval of the script just change the line at the bottom that says time.sleep(300). this means the default interval is 300 seconds (5 minutes). but you can change that if you want. If your openweathermap account is using the free plan, make sure to not exceed 60 calls per minute.

you can run this both locally or on a service like heroku, just make sure that whatever service you use won't rate limit you and you have enough hours in it to keep it running for as long as you like. heroku gives free users 450 hours per month, idk about other services
