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
    channel = client.get_channel(604320261306843166)   
    person_count = len([member for member in member.guild.members if not member.bot])
    embed = discord.Embed(title=f'Welcome {member.name} to {member.guild.name}', description='**__Thanks for Joining__**', color=0X27ece1)
    embed.set_thumbnail(url=member.avatar_url) 
    embed.set_image(url=member.avatar_url)
    embed.add_field(name='__Join position__', value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name='Time of joining', value=member.joined_at.date(), inline=True)
    await channel.send(channel, embed=embed)	
        

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def information(ctx):
    rule_1 = "The head honchos of the server.\n<@591996301311213598>"
    rule_2 = "The senior staff members of the server, these users solve staffs' problems, and manages the server's activities.\n<@586190462331912192>\n<@498378677512437762>"
    rule_3 = "These users keep the server safe from harm and should be the first people you message should you need help.\n<@436422568849702942>\n<@603586663033077760>"
    rule_4 = "These users are the junior staff members, who moderate the chats and delete inappropriate messages.\n<@482954978236039171>\n<@584275856256401418>\n<@543703851119935489>"
    embed = discord.Embed(title="**STAFF ROLES**", description="These people ensure that the usage of this environment reflects the guidelines as illustrated in the rules. Staff are sometimes handpicked, and sometimes there is an application process. They help to moderate and enhance the server, and always have the final decision.", color=0X333331)
    embed.add_field(name="OWNER", value=rule_1, inline=False)
    embed.add_field(name="ADMINISTRATOR", value=rule_2, inline=False)
    embed.add_field(name="SENIOR MODERATOR", value=rule_3, inline=False)
    embed.add_field(name="CHAT MODERATOR", value=rule_4, inline=False)
    await ctx.send(embed=embed)
	

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def links(ctx):
    rule_1 = "https://discord.gg/gdK3xBN"
    rule_2 = "<@608978244582244365> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=608978244582244365&permissions=130065&scope=bot)"
    rule_3 = "<@592988250591985715> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=592988250591985715&permissions=8&scope=bot)"
    embed = discord.Embed(title="EXTERNAL LINKS", description="In this section, you will find some of the common links related to the server.", color=0X27ece1)
    embed.add_field(name="Server Invite link", value=rule_1, inline=False)
    embed.add_field(name="POKECORD GURU invite link", value=rule_2, inline=False)
    embed.add_field(name="CRY N____invite link", value=rule_3, inline=False)
    await ctx.send(embed=embed)

			   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def rules(ctx):
    rule_1 = ":fire: Follow and Respect the Rules :fire:\n:fire: Respect all members at all times.\n:fire: No spam or advertising of other Discord servers.\n:fire: No mic spam or voice channel annoyance (this goes for hopping too)\n:fire: No PM harassment (suggest you modify your privacy settings to prevent any occurrences).\n:fire: No racism or bigotry allowed.\n:fire: No begging for roles or permissions.\n:fire: No marketing, this is not the place to sell anything.\n:fire: No 'self-bots' these are quite an annoyance.\n:fire: Do not argue with members of staff, their decision is final.\n:fire: No staff impersonation\n:fire: Don't Do Dm Advertise Or You got A Permanent Ban.\n:fire: No spam  advertising of your Discord servers.\n:fire: Do not use bot commands in any other channel than <#605305731209494528>.\n\nx-----------------------ThankYou !!! :D-----------------------x"
    embed = discord.Embed(title="SERVER RULES", description=None, color=0X27ece1)
    embed.add_field(name="🛡️ Have a Great Time Here in This Discord Server 🛡️", value=rule_1, inline=False)
    await ctx.send(embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def membership(ctx):
    rule_1 = "Benefits- \n<a:tick:625567997146431520> 25% off in <#609196821071527956> \n\n<a:tick:625567997146431520> Snipe freely in channels \n\n<a:tick:625567997146431520> Receive 3 invites Free in each invite contest \n\n<a:tick:625567997146431520> Get access to custom chat room where are you can invite your friends \n\n<a:tick:625567997146431520> Membership includes all passes including the ones we add in future at no extra cost to you \n\nCost- \n:moneybag: 100,000 credits for lifetimes \n\n:moneybag: 20,000 credits for 1 month \n\n:moneybag: 10,000 credits for 1 weekly \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    embed = discord.Embed(title="MIMIKIYU WORLD MEMBERSHIP", description=None, color=0X27ece1)
    embed.add_field(name="<a:124:625571171366338571> What is Mimikiyu World Membership? \nMimikyu membership is a membership for this server which grants you some special features then normal users for monthly/lifetime!", value=rule_1, inline=False)
    await ctx.send(embed=embed)	
			   
		
client.run(os.getenv('TOKEN'))
