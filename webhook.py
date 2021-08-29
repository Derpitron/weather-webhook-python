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
		#Setting up the variables
		data1 = get(os.getenv("API1")).json()
		data2 = get(os.getenv("API2")).json()
		data3 = get(os.getenv("API3")).json()
		if ('rain' in data1):
			isRaining = 'rain' in data1
			rainFallQuantity = data1['rain']['1h']
		if ('rain' in data2):
			isRaining = 'rain' in data2
			rainFallQuantity = data2['rain']['1h']
		if ('rain' in data3):
			isRaining = 'rain' in data3
			rainFallQuantity = data3['rain']['1h']

		#The meat and potatoes of this program
		if (isRaining == True):
			if firstRun == False:
				isRainingTest = False
			if (isRaining != isRainingTest):
				if (rainFallQuantity >= os.getenv('RAINQUANTITY')): #If the rainfall quantity is equal to or more than 1.50mm
					hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
			isRainingTest = isRaining
			firstRun = True
		time.sleep(int(os.getenv('INTERVAL')))

except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")