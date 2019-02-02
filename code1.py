import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp		

client = commands.Bot(description="marcos bot", command_prefix=commands.when_mentioned_or("*"), pm_help = True)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')

@client.command(pass_context = True)
async def lovedetect(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('```Proper usage is \n!!lovedetect @user1 @user2```')
        
	
@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(title="command Prefix: !! ", color=0Xf9fcfc)
    embed.add_field(name="__**administrator commands**__", value="`serverinfon  :` server's information (Administrator). \n`membercount  :`how many servers mamber in. \n`poll  :` Polling (Administrator). \n`ban  :` ban the user. \n`clear  :` clear messages(Administrator). \n`announce  :` To announce the entered **#channel** n **matter** (Administrator). ", inline=True)
    embed.add_field(name="__**music commands**__", value="`play  :` play the music you want. \n`pause  :` will pause the audio. \n`resume  :` will resume the audio. \n`skip` - will skip the music. \n`stop` -  will Bot disconnected. \n`song` - To Check The Current playing song. ") 
    embed.add_field(name="__**animals commands**__", value="`fox  :` This will show a fox images. \n`dog` - This will show a dog images. \n`cat` - this will show a cat images. \n`bird` - this will show a bird images. ")
    embed.add_field(name="__**games commands**__", value="`rps  :` This will play the rock, paper and scissors.\n`rolldice` - This will roll the dice and get 1 to 6 numbers. \n`flipcoin` - This will flip the coin. ")
    embed.add_field(name="__**fun commands**__", value="`virus  :` This will virus the user. \n`jpke` - this will tell you a joke.")
    embed.add_field(name="__**information commands**__", value="`botinfo  :` Information about this BOT \n`userinfo` - This will show the user's information. \n`ping` - This will show your ping.")
    embed.add_field(name="__**images commands**__", value="`meme  :` This will show a meme image. \n`avatar` -  Avatar of mentioned user. \n`dc` -  Random DC GIF \n`marvel` - Random Marvel GIF. \n`joker` - Random Joker GIF. \n`slap` - this will slap the user. \n`hug` -  this will hug a user. \n`kiss` - this will kiss the user. \n`lovedetect` - This will show how the users love each other.  \n\n__support server__ - [click here](https://discord.gg/dFM9HG6) \n__bot invite__ - [click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot) \n\n__**more feautures coming soon...**__")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532751889172004865/540387622418251780/100.gif') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)  

client.run(os.getenv('Token')) 
