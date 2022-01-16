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
  
    @bot.on(events.NewMessage(pattern="^/memes))
    async def ids(event):
      data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
      images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

#List all the memes
      await event.reply("""**Here is the list of available meme Temps :**
      
      
1 Drake Hotline Bling
2 Two Buttons
3 Distracted Boyfriend
4 Running Away Balloon
5 Left Exit 12 Off Ramp
6 UNO Draw 25 Cards
7 Buff Doge vs. Cheems
8 Change My Mind
9 Gru's Plan
10 Bernie I Am Once Again Asking For Your Support
11 Batman Slapping Robin
12 Woman Yelling At Cat
13 Waiting Skeleton
14 Expanding Brain
15 Epic Handshake
16 Disaster Girl
17 Sad Pablo Escobar
18 Boardroom Meeting Suggestion
19 Tuxedo Winnie The Pooh
20 I Bet He's Thinking About Other Women
21 Monkey Puppet
22 Panik Kalm Panik
23 Always Has Been
24 Mocking Spongebob
25 Clown Applying Makeup
26 Hide the Pain Harold
27 X, X Everywhere
28 Blank Nut Button
29 They're The Same Picture
30 Guy Holding Cardboard Sign
31 Bike Fall
32 Inhaling Seagull
33 Is This A Pigeon
34 One Does Not Simply
35 This Is Fine
36 The Scroll Of Truth
37 Ancient Aliens
38 Roll Safe Think About It
39 Success Kid
40 American Chopper Argument
41 Laughing Leo
42 Surprised Pikachu
43 Marked Safe From
44 The Rock Driving
45 Y'all Got Any More Of That
46 This Is Where I'd Put My Trophy If I Had One
47 Oprah You Get A
48 Sleeping Shaq
49 Who Killed Hannibal
50 Evil Kermit
51 Unsettled Tom
52 Finding Neverland
53 Hard To Swallow Pills
54 Third World Skeptical Kid
55 Leonardo Dicaprio Cheers
56 Grandma Finds The Internet
57 Spongebob Ight Imma Head Out
58 Trump Bill Signing
59 Futurama Fry
60 Doge
61 The Most Interesting Man In The World
62 Look At Me
63 Star Wars Yoda
64 Brace Yourselves X is Coming
65 Bad Luck Brian
66 Cute Cat
67 Imagination Spongebob
68 That Would Be Great
69 Laughing Men In Suits
70 But That's None Of My Business
71 See Nobody Cares
72 First World Problems
73 Don't You Squidward
74 Oprah You Get A Car Everybody Gets A Car
75 I'll Just Wait Here
76 Uncle Sam
77 I Should Buy A Boat Cat
78 Jack Sparrow Being Chased
79 Afraid To Ask Andy
80 X All The Y
81 Yo Dawg Heard You
82 Grumpy Cat
83 Third World Success Kid
84 I'm The Captain Now
85 Scared Cat
86 Matrix Morpheus
87 Say it Again, Dexter
88 Who Would Win?
89 Mugatu So Hot Right Now
90 Too Damn High
91 Shut Up And Take My Money Fry
92 Y U No
93 Marvel Civil War 1
94 Squidward
95 Car Salesman Slaps Roof Of Car
96 Me And The Boys
97 Maury Lie Detector
98 Happy Star Congratulations
99 Simba Shadowy Place
100 Blank Transparent Square
      
      """)
      await event.reply("test")









bot.start()
bot.run_until_disconnected()
