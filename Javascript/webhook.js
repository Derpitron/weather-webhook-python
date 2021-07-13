const config = require('./config.json');
const webhook = require("webhook-discord");

const hook = new webhook.Webhook("https://discord.com/api/webhooks/864098878671814666/Kwu2gG373bBfWIR8t40cWb36bQgKdwHr9C-YfgnqYAVIiJHT9b_CKfEbfbgjfsV4yvE2");
const url = ('http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric');


while (true) {
		fetch(url)
		.then((response) => {return response.json();});

		var data = JSON.parse(response.json);
		var weatherID1 = data['weather'][0]['id'];
		var cloud1 = data['clouds']['all'];
		const validWeather = ["200","201","202","210","211","212","221","230","231","232","300","301","302","310","311","312","313","314","321","503","504","511","520","521","522","530"];

		function rainCheck() {
			if (validWeather.includes(weatherID1)) {
				hook.send("THE CLOUD HAS ARIVED");
				hook.send("JJJJJJJJJJJJJJJJ");
			}
		}

		function cloudCheck() {
			if ((cloud >= 85) && (cloud <= 100) && (validWeather.includes(weatherID1) === false)) {
				hook.send("DARKNESS RISES");
			}
		}

		function send() {
			rainCheck();
		}

		send();
		
}