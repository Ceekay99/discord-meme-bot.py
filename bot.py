import os
from dotenv import dotenv_values
import commands as com
from discord.ext import commands, tasks
from discord import app_commands
import discord
from util import meme_getter, meme_getter_ar
config = dotenv_values(".env")
TOKEN = config['TOKEN']

class MyBot(discord.ext.commands.Bot):
    async def on_ready(self):
        await self.tree.sync()


intents = discord.Intents.default()
bot: discord.ext.commands.Bot = MyBot(command_prefix='.', intents=intents)


@bot.tree.command(description="Send memes (default 10, max 50)")
async def memes(interaction: discord.Interaction, amount: int = 10):
    await com.multiple_memes(interaction, amount)

@tasks.loop(hours=24)
async def memesDailyloop():

  #print("is the function being called")
  print("Daily Memes Loop has started") 
  amount = 10
  amount_ar = 3
  guilds = bot.guilds


  for guild in guilds:

   for channel in guild.channels:

    if channel.name == "test" or channel.name == "memes":

      urls = meme_getter.meme_urls(amount)

      #urls.pop(0)

      for url in urls:
        await channel.send(url)
    elif  channel.name == "ساعه-لقلبك":
      urls = meme_getter_ar.meme_urls(amount_ar)

      #urls.pop(0)

      for url in urls:
        await channel.send(url)
       

      
@bot.event
async def on_ready():
    print("bot has started")
    memesDailyloop.start()
    
bot.run(TOKEN)
