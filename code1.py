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

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="TESTING BOT", command_prefix=commands.when_mentioned_or("*"), pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started pubg') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='BETA VERSION', type=2)) #add_your_bot_status_here



@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(title="command Prefix: !! ", color=0Xf9fcfc)
    embed.add_field(name="__**bot commands**__", value="`serverinfo` - This will show the server's information (Administrator). \n`poll` - Polling (Administrator). \n`clear<number>` - will clear messages(Administrator). \n`announce` - To announce the entered **#channel** n **matter** (Administrator). \n\n`botinfo` - Information about this BOT  \n`userinfo` - This will show the user's information. \n`lovedetect<@user1><@user2>` - This will show how the users love each other. \n`ping` - This will show your ping. \n`slap` - This will slap the user. \n`hug` -  This will hug a user. \n`kiss` - This will kiss the user. \n`joke` - This will tell you a joke. ", inline=True)
    embed.add_field(name="__**music commands**__", value="`play` - This will play the audio you want. \n`pause` - will pause the audio. \n`resume` - This will resume the audio. \n`skip` - will skip the music. \n`stop` -  will Bot disconnected. \n`song` - To Check The Current playing song. ") 
    embed.add_field(name="__**animals commands**__", value="`fox` - This will show a fox images. \n`dog` - This will show a dog images. \n`cat` - This will show a cat images. \n`bird` - This will show a bird images. ")
    embed.add_field(name="__**games commands**__", value="`rps` - This will play the rock, paper and scissors.\n`rolldice` - This will roll the dice and get 1 to 6 numbers. \n`flipcoin` - This will flip the coin. \n\n\n__support server__ - [click here](https://discord.gg/dFM9HG6) \n__bot invite__ - [click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot) \n\n__**more feautures coming soon...**__")
    embed.add_field(name="__**images commands**__", value="`meme` - This will show a meme image. \n`avatar` -  Avatar of mentioned user. \n`marvel` - Random Marvel GIF. \n`joker` - Random Joker GIF. \n`")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532751889172004865/540387622418251780/100.gif') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)   

	
client.run(os.getenv('Token'))

