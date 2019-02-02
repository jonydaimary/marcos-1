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
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')

@client.command(pass_context = True)
async def lovedetect(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('```Proper usage is \n!!lovedetect @user1 @user2```')
        
	
@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(color=0Xf9fcfc)
    embed.set_author(name="Command prefix: !!")
    embed.add_field(name="__Administrator commands__", value="`serverinfo  :` server's information . \n`membercount  :` how many servers mamber in. \n`poll  :` Polling . \n`ban  :` ban the user. \n`clear  :` clear messages. \n`announce  :` To announce the entered **#channel** n **matter** . ", inline=True)
    embed.add_field(name="__Fun commands__", value="`virus  :` virus. \n`joke  :` tell you a joke ! . ")	
    embed.add_field(name="__Music commands__", value="`play  :` play the music you want. \n`pause  :` will pause the audio. \n`resume  :` will resume the audio. \n`skip  :` will skip the music. \n`stop  :` will Bot disconnected. \n`song  :` To Check The Current playing song. ") 
    embed.add_field(name="__Animals commands__", value="`fox  :` fox images. \n`dog  :` dog images. \n`cat  :` cat images. \n`bird  :` bird images. ")
    embed.add_field(name="__Games commands__", value="`rps  :` play the rock, paper and scissors.\n`rolldice  :` roll the dice and get 1 to 6 numbers. \n`flipcoin  :` flip the coin. ")
    embed.add_field(name="__Information commands__", value="`botinfo  :` Information about this BOT. \n`userinfo  :` user's information. \n`ping  :` pong.")
    embed.add_field(name="__Images commands__", value="`meme  :` meme image. \n`avatar  :` Avatar. \n`dc  :` DC GIF \n`marvel  :` Marvel GIF. \n`joker  :` Joker GIF. \n`slap  :` slap the user. \n`hug  :`  hug a user. \n`kiss  :` kiss the user. \n`lovedetect  :` lovedetect.  \n\n__support server__ - [click here](https://discord.gg/dFM9HG6) \n__bot invite__ - [click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot) \n\n__**more feautures coming soon...**__")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532751889172004865/540387622418251780/100.gif') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)  

@client.command(pass_context = True)
async def dc(ctx):
    choices = ['https://media.giphy.com/media/uDPSXySAEDv56/giphy.gif', 'https://media.giphy.com/media/26vIg1DlkNdJr65q0/giphy.gif', 'https://media.giphy.com/media/jcIRoyJKQG3za/giphy.gif', 'https://media.giphy.com/media/26xBLVi4RuhYmV6zm/giphy.gif', 'https://media.giphy.com/media/xUOwGfcrlRjKjs2sSI/giphy.gif', 'https://media.giphy.com/media/l41Yq5KYEmbxFaeVq/giphy.gif', 'https://media.giphy.com/media/3o7abJW5ZuiByDelji/giphy.gif', 'https://media.giphy.com/media/xU67CtAMi8f5K/giphy.gif', 'https://media.giphy.com/media/VXQuKHDhTIBWM/giphy.gif']
    embed=discord.Embed(title="Here's Your dc GIF {}".format(ctx.message.author.name), color=0Xf9fcfc)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532751889172004865/540387622418251780/100.gif')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)

		
@client.command(pass_context = True)
async def joker(ctx):
    choices = ['https://media.giphy.com/media/KZd26L2o8QXtK/giphy.gif', 'https://media.giphy.com/media/aazZrFTMrDKLK/giphy.gif', 'https://media.giphy.com/media/F0A48Q2wFjE7S/giphy.gif', 'https://media.giphy.com/media/7waKDy5RbDYVG/giphy.gif', 'https://media.giphy.com/media/13m24iFmhomZi0/giphy.gif', 'https://media.giphy.com/media/zCP1GdPjxtCTe/giphy.gif', 'https://media.giphy.com/media/tN2OR1R1BLKV2/giphy.gif', 'https://media.giphy.com/media/X9Z0O2bpi8GMU/giphy.gif', 'https://media.giphy.com/media/YPIrsRqqO7oB2/giphy.gif', 'https://media.giphy.com/media/FSp1Wqx2TPYSA/giphy.gif', 'https://media.giphy.com/media/8UwEdwAF5XWQE/giphy.gif']
    embed=discord.Embed(color=0Xf9fcfc)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)
			
@client.command(pass_context = True)
async def marvel(ctx):
    choices = ['https://media.giphy.com/media/F9hQLAVhWnL56/giphy.gif', 'https://media.giphy.com/media/l4FGrYKtP0pBGpBAY/giphy.gif', 'https://media.giphy.com/media/JzujPK0id34qI/giphy.gif', 'https://media.giphy.com/media/M9TuBZs3LIQz6/giphy.gif', 'https://media.giphy.com/media/3GnKKEw2v7bXi/giphy.gif', 'https://media.giphy.com/media/GR1WWKadM9m0g/giphy.gif', 'https://media.giphy.com/media/iBpq5SbrYiSTTSHO7z/giphy.gif', 'https://media.giphy.com/media/dJirXKRo0j1l0j9V9Q/giphy.gif', 'https://media.giphy.com/media/ZvkFmclQO1ImmRNm0K/giphy.gif', 'https://media.giphy.com/media/82Mksc7tnX3qp4FVNN/giphy.gif', 'https://media.giphy.com/media/mTQhl6cWXDJBu/giphy.gif']
    embed=discord.Embed(color=0Xf9fcfc)
    embed.set_footer(text=f'Requested by {ctx.message.author.name} ', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)
	

client.run(os.getenv('Token')) 
