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

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0xf9fcfc)
client = commands.Bot(description="marcos bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)

client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='!!help | marcos.#0290', type=2)) 
        await asyncio.sleep(120)
        await client.change_presence(game=discord.Game(name='BETA VERSION')) 
        await asyncio.sleep(120)
        await client.change_presence(game=discord.Game(name='with ' +str(len(set(client.get_all_members())))+' users', type=3))
        await asyncio.sleep(120)
		
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')
    client.loop.create_task(status_task())
	
	
client.run(os.getenv('Token')) 
