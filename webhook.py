import time
from datetime import datetime
import os
from socket import gethostname
from traceback import format_exc

from dhooks import Webhook
from dotenv import load_dotenv
from pytz import timezone
from requests import get

load_dotenv()
debug = Webhook(os.getenv('DEBUG'))
localtz = datetime.now(timezone(os.getenv('TIMEZONE')))
try:
	hook = Webhook(os.getenv('HOOK'))
	firstRun = False
	debug.send("Script started on " + gethostname() + " with process ID: `" + str(os.getpid()) + "` at " + os.getenv('TIMEZONE') + " - " + localtz.strftime('%H:%M:%S') + " with interval of `" + os.getenv('INTERVAL') + "` seconds")
	while True:
		data1 = get(os.getenv("API1")).json()
		data2 = get(os.getenv("API2")).json()
		data3 = get(os.getenv("API3")).json()
		isRaining1 = 'rain' in data1
		isRaining2 = 'rain' in data2
		isRaining3 = 'rain' in data3
		if ('rain' in data1):
			isRaining = 
		if ('rain' in data2):
			isRaining = isRaining2
		if ('rain' in data3):
			isRaining = isRaining3

		if (isRaining == True):
			if firstRun == False:
				isRainingTest = False
			if (isRaining != isRainingTest):
				if ( >= 1.50):
					hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
			isRainingTest = isRaining1
			firstRun = True
		time.sleep(int(os.getenv('INTERVAL')))

except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")