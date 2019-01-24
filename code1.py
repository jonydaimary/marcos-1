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
async def hack(ctx, user: discord.Member):
    """Hack someone's account! Try it!"""
    text = await Utils.clean_text(ctx, str(user))
    msg = await ctx.send(f"Hacking! Target: {text}")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files... [▓▓    ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
    await asyncio.sleep(2)
    await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
    await asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
    await asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
    await asyncio.sleep(4)
    await msg.edit(content=f"An error has occurred hacking {text}'s account. Please try again later. ❌")   
   
@client.command(pass_context = True)
async def hack2(ctx, user: discord.Member*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    await msg.edit(content="Accessing Discord Files... [▓▓    ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
    await asyncio.sleep(2)
    await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
    await asyncio.sleep(2)
    await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
    await asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
    await asyncio.sleep(3)
    await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
    await asyncio.sleep(4)
    await msg.edit(content=f"An error has occurred hacking {text}'s account. Please try again later. ❌")   
   


client.run(os.getenv('Token'))

