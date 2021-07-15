import time
from os import getenv
from requests import get
from dhooks import Webhook
from dotenv import load_dotenv
from socket import gethostname
from datetime import datetime
from pytz import timezone
localtz = datetime.now(timezone('TIMEZONE'))
load_dotenv()
hook = Webhook(getenv('HOOK'))
debug = Webhook(getenv('DEBUG'))
debug.send("Script started on " + gethostname() + " at " + localtz.strftime('%H:%M:%S'))
x = False
while True:
	try:
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
			print(x)
			x = True
		time.sleep(30)
	except Exception as error:
		debug.send(error)