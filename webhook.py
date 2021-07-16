import time
from os import getenv
from requests import get
from dhooks import Webhook
from dotenv import load_dotenv
from socket import gethostname
from datetime import datetime
from pytz import timezone
from traceback import format_exc
load_dotenv()
debug = Webhook(getenv('DEBUG'))
localtz = datetime.now(timezone(getenv('TIMEZONE')))
try:
	hook = Webhook(getenv('HOOK'))
	x = False
	debug.send("Script started on " + gethostname() + " at " + getenv('TIMEZONE') + " - " + localtz.strftime('%H:%M:%S') + " with interval of `" + getenv('INTERVAL') + "` seconds")
	while True:
		response = get(getenv('API'))
		data = response.json()
		isRaining = "rain" in data
		if isRaining:
			if x == False:
				isRainingTest = False
			def rainCheck():
				if ((isRaining) and (isRaining != isRainingTest)):
					hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
			isRainingTest = isRaining
			rainCheck()
			x = True
		if isRaining:
			debug.send("It is currently raining according to OpenWeatherMap")
		else:
			debug.send("It is not currently raining according to OpenWeatherMap")
		time.sleep(int(getenv('INTERVAL')))
except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + "`" + getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")