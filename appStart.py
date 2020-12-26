import os
# Use the package we installed
import logging
import random

from slack_bolt import App, Say, BoltContext
from slack_sdk import WebClient

logging.basicConfig(level=logging.DEBUG)

tips = [
    "Always make sure that you update the Request URL when restarting ngrok",
    "Make sure you check your scopes when an API method does not work",
    "Every API call has a scope check that you use the correct ones and when calling something new add that scope on Slack",
    "After changing the scope you need to install your App again",
    "Every Event you want to use, you need to subscribe to on Slack",
    "Every Slack command needs the Request URL",
    "The Bot token is on the Basics Page",
    "The Slack Signing Secret is on the OAuth & Permission page",
    "Limit the scopes to what you really need",
    "You can add collaborators to your Slack App under Collaborators, they need to be in the workspace",
    "To use buttons you need to enable Interactive Components",
    "Always go in tiny steps, use the logger or print statements to see where you are and if events reach your app",
    "If the user does something on Slack always send a response, even if it is just an emoji",
    "Your App can use on the users behalf, you need to get User Scopes in that case. Later this would lead to having to save user tokes",
    "Do not plan to much, do simple things first, when you get these done then start to dream big",
    "Storing persistent data in a DB makes sense, when you are not familiar with it maybe a dict in a file might be enough for now",
    "Oauth -- so authenticating the app and user is important when distributing your app, while locally developing it is not that important yet, get some functionality going first",
    "Have the Slack API, Slack Events and your Slack Build App page open in your browser to have fast access",
    "Slash commands need to be unique in a workspace, so do append your bots name to them"
]

# Initialize app with bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_mention")
def app_mentioned(body, event, logger, say, client):
    logger.info("Testing app_mention\n")
    #logger.info(body)
    channelList = client.conversations_list()
    logger.info(channelList)

    say(f"Hello there <@{event['user']}>")
    client.chat_postEphemeral(channel=event['channel'], user=event['user'], text="Feel free to ask me anything!")

@app.command("/sb2.0_tips")
def tips_called(ack, body, command, logger, client):
    ack()
    logger.info("Testing slackbot2.0_tips")
    logger.info(command)
    tip = random.choice(tips)

    block = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Tip: "
                    }
                }
            ]
    attach= [
                {
                    "color": "#f2c744",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": tip
                            }
                        },
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Show more Slack API tips",
                                        "emoji": True
                                    },
                                    "value": "click_me_123",
                                    "action_id": "show_more_tips"
                                }
                            ]
                        }
                    ]
                }
            ]

    client.chat_postMessage(channel=command['channel_id'], blocks=block, attachments=attach)

@app.action("show_more_tips")
def tip_button_clicked(body, action, ack, logger):
    ack()
    logger.info("Testing tip_button_clicked")
    logger.info(action)

# Start app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))