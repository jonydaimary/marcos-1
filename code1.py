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


@client.event
async def on_ready():
    print('Logged in')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')

	



	

client.run(os.getenv('Token')) 
