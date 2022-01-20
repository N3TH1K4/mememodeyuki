import requests
import urllib
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

apiid = 4091096
apihash = '6bb0682b4af56456201c3b9d8b99c94a'
bottoken = '2025919134:AAGAyAXR9hTJZu6v75-5ho8ao95mcppXacU'
username = 'TROJ3N'
password = 'Nethika123'
# We have to manually call "start" if we want an explicit bot token
bot = Client("meme-bot",
             api_id=apiid,
             api_hash=apihash,
             bot_token=bottoken,)


data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 \
    Safari/537.36'
API_TEXT ="blaaa"

@bot.on_message(filters.command(commands=['meme']) & filters.private)
async def meme1(bot, msg: Message,):
    bot.reply_text(msg.chat.id,"yooo")
    api = await bot.ask(
        chat.id
    )
    if await is_cancel(msg, api.text,API_TEXT):
        return
    msg.reply_text(api)
    
bot.run()    
