# SlackBot2.0

![image](https://user-images.githubusercontent.com/33184844/103165226-db68a900-47c9-11eb-974a-010a9bd96091.png)

A simple bot created with [Slack Bolt for Python](https://api.slack.com/start/building/bolt-python) using [Slack's Event API](https://api.slack.com/events).
The app will greet new users and create an interactive modal for introductions. A basic App home was also added, with features
such as displaying tips whenever the user clicks into the App home. Tips can be generated via a slash command as well.


###### Installation:
	CD into the folder
	ngrok http 3000
	In a separate CMD shell, CD into the folder
	python -m venv .venv
	./.venv/Scripts/activate
	set SLACK_BOT_TOKEN=
	set SLACK_SIGNING_SECRET=
	pip install slack_bolt
	python appStart.py

![image](https://user-images.githubusercontent.com/33184844/103165160-fb4b9d00-47c8-11eb-816f-09f7ab70eca0.png)