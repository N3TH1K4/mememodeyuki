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
  
    @bot.on(events.NewMessage(pattern="^/memes (.*)"))
    async def ids(event):
      data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
      images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

#List all the memes
      await event.reply('Here is the list of available memes : \n')
      ctr = 1
      for img in images:
        await event.send_message(ctr,img['name'])
        ctr = ctr+1










bot.start()
bot.run_until_disconnected()
