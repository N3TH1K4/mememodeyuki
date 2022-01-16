import requests
import urllib


from telethon.sync import TelegramClient ,events ,Button
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '2025919134:AAGAyAXR9hTJZu6v75-5ho8ao95mcppXacU'
username = 'TROJ3N'
password = 'Nethika123'
# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

with bot:










bot.start()
bot.run_until_disconnected()
