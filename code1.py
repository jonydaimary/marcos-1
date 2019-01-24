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



async def req(self, url):
    res = await self.bot.session.get(f"https://nekos.life/api/v2/img/{url}")
    res = await res.json()
    return box.Box(res)
  

@client.command(pass_context = True)
async def boobs(self, ctx):
    """WARNING: NSFW command. Gets pictures of boobs."""
    if not ctx.channel.nsfw:
        return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")
    if not ctx.channel.nsfw:
        return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

    res = await self.req("boobs")
    embed = discord.Embed(color=0Xf9fcfc, title="Boobs :eggplant: ")
    embed.set_image(url=res.url)
    embed.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)



client.run(os.getenv('Token'))

