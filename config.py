from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"اب ايديك")
APP_HASH = os.environ.get("APP_HASH",
"هاشك")
BOT_USERNAME = os.environ.get("BOT_USERNAME",
                           "يوزر بوتك بدون @")
session = os.environ.get("TERMUX",
                        "تيرمكسك")
SESSION = os.environ.get("TERMUX",
                        "تيرمكسك للمره الثانيه")
token = os.environ.get("TOKEN",
                      "توكنك")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
