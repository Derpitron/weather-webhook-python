# Discord Weather Webhook - Python Flavor
This is a script which pulls current weather from OpenWeatherMap and if it is raining, then it sends a message to a specified Discord webhook. 

# Unique features of this script?
This script allows you to change the interval of the script, change variables, and it sends a start message with the name of the host and local time, as well as any caught exceptions to a debug webhook you specify. It also has a feature where it does not send the message until and unless the weather changes from not-raining to raining. (this part took me much longer than i'd like to figure out.)

# Installation
clone the repository, cd into it, pip install -r requirements.txt

# Variables
In .env change the placeholders to: your main Discord webhook link, OpenWeatherMap api link (note: this script was built with the OpenWeatherMap Current Weather API in mind so dont use any other API. also use latitude and longitude of your location), debug webhook link to send start and error messages to, and your timezone in Time Zone Database format.

# Change interval of script
If you want to change the interval of the script just change the line at the bottom that says time.sleep(30). This means the default interval is 30 seconds (Half a minute), but you can change that. If your OpenWeatherMap account is using the free plan, make sure to not exceed 60 calls per minute.

# How to use it?
Run webhook.py once you've made the necessary changes.  You can run this both locally or on a service like Heroku, just make sure that whatever service you use won't rate limit you and you have enough hours in it to keep it running for as long as you like. Heroku gives free users 450 hours per month, but check with the service you're using!

Star this repo, and follow me and Vishard-006 for more cool projects like these!
