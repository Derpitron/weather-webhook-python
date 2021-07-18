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
	x = False
	debug.send("Script started on " + gethostname() + " with process ID: `" + str(os.getpid()) + "` at " + os.getenv('TIMEZONE') + " - " + localtz.strftime('%H:%M:%S') + " with interval of `" + os.getenv('INTERVAL') + "` seconds")
	while True:
		response = get(os.getenv("API"))
		data = response.json()
		isRaining = 'rain' in data
		if (isRaining == True):
			if x == False:
				isRainingTest = False
			if ((isRaining == True) and (isRaining != isRainingTest)):
				hook.send("THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ")
			isRainingTest = isRaining
			x = True
		time.sleep(int(os.getenv('INTERVAL')))
except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + "`" + os.getenv('TIMEZONE') + "`" + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")