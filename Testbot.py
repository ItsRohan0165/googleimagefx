import discord
from discord import utils, Client
from discord.ext import commands
import random

from googleapiclient.discovery import build
import pprint
import asyncio
import os


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
client = commands.Bot(command_prefix='!',description=description)

@client.event
async def on_ready():
    print('Logged in as')
   

@client.command(pass_context=False)
async def google(*text: str):
    finaltext = ' '
    for word in text:
        finaltext = finaltext + word  + " "
    
    api_key = (os.getenv("API"))
    cse_id = (os.getenv("CSE"))
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']    
    results = google_search(finaltext, api_key, cse_id, num=3)
    for result in results:
        formatText="*" + result['snippet'] + "*"
        await ctx.send(formatText)
@client.command(pass_context=False)
async def gimg(*text : str):
    print('got here')

    """Searches google for an image described by input"""
    finaltext = " "
    
    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = " "
    cse_id = " "

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        formatText = "" + result['link'] + ""
        await ctx.send(formatText)
@client.command()
async def jimmy():
    """In case I'm not here obviously"""
    random.seed()
    
@client.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@client.command()
async def Tides():
    """How quickly the tides turn"""
    await ctx.send("http://i1.kym-cdn.com/photos/images/original/001/072/409/23c.gif")
#@asyncio.coroutine
#def on_message(message):
    #yield from self.process_commands(message)
   # if("jimmy" in message.content ):
        #foo=random.choice(["day seven. still have not finished the binding of isaac", "NEVER SHOULD HAVE COME HERE", "YOU'VE VIOLATED MY MOTHER!", "PICKED A BAD TIME TO GET LOST FRIEND", "You'll MAKE A FINE RUG, CAT", "Am I supposed to stand idly by WHILE A DRAGON BURNS MY HOLD AND SLAUGHTERS MY PEOPLE!?","porque no los dos","tough love is the only love","ukraine is game to you!?","https://i1.rgstatic.net/ii/profile.image/AS%3A272457688940593@1441970383991_l/Mike_Roggenkamp.png ","Don't mind me, just taking my hotdogs for a walk ( ͡° ͜ʖ ͡°)╯╲___ :hotdog:","( ͡° ͜ʖ ͡°)╯╲___卐卐卐卐","http://coolaustralia.org/wp-content/uploads/2013/05/billandwill.jpg","Remember the playlist!", "I blame Sean personally.", ".play seinfeld in the trap", "Don't forget I hate you all", "Don't forget you're here forever", "have you tried turning it on and off again", "that's the dumbest shit I've heard today.", "delete that fucking bird right now I swear to god", "nice microphone quality", "get a headset", "I might be a nazi mod but at least I'm not the one posting shit", "beep boop sean is a ro-bot", "arma 3 isn't a game it's a tactical simulator", "that's XCOM baby", "not my fault you're shit at games", "My anime is better than yours, by virtue of how awful it is"])
        #channel.send( foo, tts=1)
    #print('bloop')
client.run(os.getenv('TOKEN'))
