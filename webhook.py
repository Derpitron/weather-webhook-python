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
	debug.send("Script started successfully on " + gethostname() + " at " + localtz.strftime('%H:%M:%S'))
	while True:
		response = get(getenv('API'))
		data = response.json()
		if 'rain' in data:
			rainData = data['rain']
			isRaining = 'rain' in rainData
			if x == False:
				isRaining2 = False
			def rainCheck():
				if ((isRaining) and (isRaining != isRaining2)):
					hook.send('THE CLOUD HAS ARIVED\nJJJJJJJJJJJJJJJJ')
			isRaining2 = isRaining
			rainCheck()
			x = True
		time.sleep(int(getenv('INTERVAL')))
except Exception:
	error = format_exc()
	debug.send("Script failed on " + gethostname() + " at " + localtz.strftime('%H:%M:%S'))
	debug.send("```" + error + "```")