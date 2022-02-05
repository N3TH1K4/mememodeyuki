import requests
import asyncio
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
bottoken = '2025919134:AAEiMUp8gZ3W2QD-YAgDpGZXcYol_RfEPWg'
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
@bot.on_message(filters.command(commands=['meme1']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Drake Hotline Bling\n`Template ID`: 1")
    id = 1
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
@bot.on_message(filters.command(commands=['meme2']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Two Buttons\n`Template ID`: 2")
    id = 2
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
    
    
@bot.on_message(filters.command(commands=['meme3']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Distracted Boyfriend\n`Template ID`: 3")
    id = 3
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
    
@bot.on_message(filters.command(commands=['meme4']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Running Away Balloon\n`Template ID`: 4")
    id = 4
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
    
@bot.on_message(filters.command(commands=['meme5']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: UNO Draw 25 Cards\n`Template ID`: 5")
    id = 5
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
    
@bot.on_message(filters.command(commands=['meme6']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Left Exit 12 Off Ramp\n`Template ID`: 6")
    id = 6
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
    
@bot.on_message(filters.command(commands=['meme7']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Buff Doge vs. Cheems\n`Template ID`: 7")
    id = 7
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

@bot.on_message(filters.command(commands=['meme8']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Change My Mind\n`Template ID`: 8")
    id = 8
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
    
@bot.on_message(filters.command(commands=['meme9']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Gru's Plan\n`Template ID`: 9")
    id = 9
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

@bot.on_message(filters.command(commands=['meme10']))
async def meme1(bot, msg: Message):
    chat = msg.chat
    await bot.send_message(chat.id,"**Meme Generator @Yukinonthecutebot**\n\n`Template`: Bernie I Am Once Again Asking For Your Support\n`Template ID`: 10")
    id = 10
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
    await bot.send_photo(chat.id,filename,caption="Powered By @waifuNetwork)    
    
bot.run()    
