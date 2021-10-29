import time
from datetime import datetime
import os
from socket import gethostname
from traceback import format_exc

from dhooks import Webhook
from dotenv import load_dotenv
from pytz import timezone
from requests import get

def main():
	load_dotenv()
	debug = Webhook(os.getenv('DEBUG'))
	localtz = datetime.now(timezone(os.getenv('TIMEZONE')))
	try:
		hook = Webhook(os.getenv('HOOK'))
		firstRun = True #When the script is run for the first time
		debug.send("Script started on " + gethostname() + " with process ID: `" + str(os.getpid()) + "` at " + os.getenv('TIMEZONE') + " - " + localtz.strftime('%H:%M:%S') + " with interval of `" + os.getenv('INTERVAL') + "` seconds")
		while True:
			#Setting up the variables
			data1 = get(os.getenv("API1")).json()
			data2 = get(os.getenv("API2")).json()
			data3 = get(os.getenv("API3")).json()
			rainData = ['data1', 'data2', 'data3']
			isRaining = any(rainData)
			#rainFallQuantities of each weather source
			if ('rain' in data1):
				rainFallQuantity = data1['rain']['1h']
			elif ('rain' in data2):
				rainFallQuantity = data2['rain']['1h']
			elif ('rain' in data3):
				rainFallQuantity = data3['rain']['1h']

			#The main part of the program
			if (isRaining == True):
				if firstRun == True:
					isRainingLastIter = False
				if (isRaining != isRainingLastIter):
					if (rainFallQuantity >= 0.30): #If the rainfall quantity is equal to or more than 0.30mm
						hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
				isRainingLastIter = isRaining
				firstRun = False
			time.sleep(int(os.getenv('INTERVAL')))

	#Error Handling
	except Exception:
		error = format_exc()
		debug.send("@everyone Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
		debug.send("```" + error + "```")

if __name__ == "__main__":
	main()