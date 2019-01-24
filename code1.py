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
client = commands.Bot(description="TEST Official Bot", command_prefix=commands.when_mentioned_or("*"), pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started pubg') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='BOT BETA TESTING')) #add_your_bot_status_here

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    if channel is None:
        await client.say(" ```Proper usage is\n\nannounce<channel><matter>```")
    else:
        embed=discord.Embed(title="Announcement", description="{}".format(msg), color = 0xf9fcfc)
        await client.send_message(channel, embed=embed)
        await client.delete_message(ctx.message)
	
   
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    if user == None:
        await client.say("```Proper usage is\n\n!!kiss <mention a user>```")
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color=0Xf9fcfc)
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)
 

client.run(os.getenv('Token'))

