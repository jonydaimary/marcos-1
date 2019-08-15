import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
from discord import Spotify
import os
import functools
import time
import datetime
import requests
import json
import aiohttp		

client = commands.Bot(description="cry n___ bot", command_prefix=commands.when_mentioned_or(">"), pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.idle)

@client.event
async def on_ready():
    print('--------')
    print('--------')
    print('Started new here ')
    print('Created by MARCOS々DMRY')
    client.loop.create_task(status_task()) 
		
@client.event
async def on_member_join(member):
    guild = client_id = "592262404071620610"
    channel = client.get_channel(593696190730862592)   
    person_count = len([member for member in member.guild.members if not member.bot])
    embed = discord.Embed(title=f'Welcome {member.name} to {member.guild.name}', description='**__Thanks for Joining__**', color=0X333233)
    embed.set_thumbnail(url=member.avatar_url) 
    embed.set_image(url=member.avatar_url)
    embed.add_field(name='__Join position__', value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name='Time of joining', value=member.joined_at.date(), inline=True)
    await channel.send(channel, embed=embed)	
        


client.run(os.getenv('TOKEN'))
