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
    if user is == None:
        await client.say(" ```Proper usage is\n\nannounce<channel><matter>```")
        return
    else:
        embed=discord.Embed(title="Announcement", description="{}".format(msg), color = 0xf9fcfc)
        await client.send_message(channel, embed=embed)
        await client.delete_message(ctx.message)

   


client.run(os.getenv('Token'))

