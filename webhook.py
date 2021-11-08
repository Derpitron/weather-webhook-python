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
			data = get(os.getenv("API")).json()
			isRaining = ('rain' in data)
			rainFallQuantity = data['rain']['1h']

			#The main part of the program
			if firstRun == True:
				isRainingLastIter = False
			if ((isRaining != isRainingLastIter) and (isRaining == True)):
				if (rainFallQuantity >= 0.30): #If the rainfall quantity is equal to or more than 0.30mm
					hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
				isRainingLastIter = isRaining
			firstRun = False
			time.sleep(int(os.getenv('INTERVAL')))

	#Error """Handling"""
	except Exception:
		error = format_exc()
		debug.send("@everyone Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S')) #Pings everyone lol
		debug.send("```" + error + "```")

if __name__ == "__main__":
	main()