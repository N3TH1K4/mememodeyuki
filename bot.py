import requests
import urllib
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyromod import listen
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired
)

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
txt1 = "**Send The First text**"
txt2 = "**Send  The Second text**"
idtxt = "**Send The Template Number**"
@bot.on_message(filters.command(commands=['meme']) & filters.private)
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**")
    idt =  await bot.ask(
        chat.id,idtxt
    )
    try:
        int(idt.text)
    except Exception:
        await idt.delete()
        await msg.reply("**Send A Number Between 1 And 100 Baaaka!**")
        return
    id = idt.text

    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
    text00 = await bot.ask(
        chat.id,txt1
    )
    text0 = text00.text
    text11 =  await bot.ask(
        chat.id,txt2
    )
    text1 = text11.text   
    print("done")
    URL = 'https://api.imgflip.com/caption_image'
    params = {
          'username':username,
          'password':password,
          'template_id':images[id-1]['id'],
          'text0':text0,
          'text1':text1
       }
    response = requests.request('POST',URL,params=params).json()
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', userAgent)
    filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')
    await bot.send_photo(chat.id,filename)
    
   
    
bot.run()    
