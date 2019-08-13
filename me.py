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


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0xf9fcfc)
client = commands.Bot(description="cry n___ bot", command_prefix=commands.when_mentioned_or(">"), pm_help = True)

client.remove_command('help')


async def task():
    while True:
        channel = client.get_channel(605305731209494528)
        address = "https://www.rrrather.com/botapi"
        data = requests.get(address).json()
        nsfw_check = data['nsfw']
        if nsfw_check == False:
            embed = discord.Embed(title=data['title'], description=f"**1){data['choicea']} \n \n2){data['choiceb']}** \n \n[Wanna know what others said about this question in www.rrrather.com? Click me...]({data['link']})", color=0xff69bf)
            embed.set_author(name="It's question time folks...", icon_url=channel.guild.icon_url)
            embed.set_footer(text=channel.guild.name)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
            await asyncio.sleep(10)
        elif nsfw_check == True:
            await asyncio.sleep(1)	
	
	
@client.event
async def on_ready():
    print('--------')
    print('--------')
    print('Started new here ')
    print('Created by MARCOS々DMRY')
	
	

@client.event
async def on_member_join(member):
    channel = client.get_channel(593696190730862592)
    person_count = len([member for member in member.guild.members if not member.bot])
    embed = discord.Embed(title=f'Welcome {member.name} to {member.guild.name}', description='**__Thanks for Joining__**', color=0X333233)
    embed.set_thumbnail(url=member.avatar_url) 
    embed.set_image(url=member.avatar_url)
    embed.add_field(name='__Join position__', value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name='Time of joining', value=member.joined_at.date(), inline=True)
    await channel.send(channel, embed=embed)	
	
	
@client.command(pass_context = True)
async def linkss(ctx):
    if ctx.message.author.id == "498378677512437762":    
        rule_1 = "https://discord.gg/gdK3xBN"
        rule_2 = "<@602824587629297664> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=602824587629297664&permissions=130065&scope=bot)"
        rule_3 = "<@592988250591985715> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=592988250591985715&permissions=8&scope=bot)"
        embed = discord.Embed(title="EXTERNAL LINKS", description="In this section, you will find some of the common links related to the server.", color=0X33f351)
        embed.add_field(name="Server Invite link", value=rule_1, inline=False)
        embed.add_field(name="POKECORD GURU invite link", value=rule_2, inline=False)
        embed.add_field(name="CRY N____invite link", value=rule_3, inline=False)
        await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))
