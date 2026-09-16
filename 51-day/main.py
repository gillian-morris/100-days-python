# Day 51 - Internet Speed Complaint Bot
# Automation on the web
from bot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()
