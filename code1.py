##IMPORTS## 
import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time

##PREFIX##
bot = commands.Bot(command_prefix='!!')

##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
 
@bot.command(pass_context=True)
async def spam(ctx, count: int, *, SecretCocoSpam: str):
    if ctx.message.author.id == "498378677512437762":
        await bot.delete_message(ctx.message)
        for i in range(count):
            await asyncio.sleep(0.20)
            await bot.say(SecretCocoSpam)

bot.run(os.getenv('Token')) 
