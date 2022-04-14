import discord
import asyncio
import random
import requests
import json
import datetime, time
from discord.ext import commands, tasks
from discord.ext import *
from discord.ext.commands import cooldown, BucketType
from discord_components import *
from copy import deepcopy
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


class Games(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(brief="See how many people get confused by the bot's typing >:)")
  async def typingtrick(self, ctx):
    await ctx.message.delete()
    async with ctx.typing():
      await asyncio.sleep(10)

  @commands.command(aliases=["rockpaperscissors"])
  async def rps(self, ctx):
    rps_bot_choice_options = ["Rock", "Paper",   "Scissors"]
    rps_bot_choice = random.choice  (rps_bot_choice_options)
  
    embed = discord.Embed(title="Rock, Paper, Scissors, Shoot!", description=f"I chose {rps_bot_choice}  !\nGG")
  
    await ctx.reply(embed=embed)

  @commands.command(aliases=["8ball", "b"])
  async def eightball(self, ctx):
    eightball_responses = ["Yes", "No", "Maybe",   "Possibly", "I think it's a yes!", "I think it's a   no.", "Uhm, I'm not too sure. Give me another   shake.", "I'd suggest yes, but it's not a   garuntee.", "I'm not too sure.", "I think you   should.", "Why not?"]
  
    embed = discord.Embed(title="The magic 8 ball   says...", description=random.choice  (eightball_responses))
  
    await ctx.reply(embed=embed)

  @commands.command(brief="Just as it seems - flip a coin", description="This command will do just as it seems - it'll flip a coin and send the result in the same channel.", aliases=["c"])
  async def coin(self, ctx):
    result = ["Heads", "Tails", "Heads", "Tails",   "Heads", "Tails", "Heads", "Tails", "Heads",   "Tails", "Heads", "Tails", "Heads", "Tails",   "Heads", "Tails", "Heads", "Tails", "Heads",   "Tails", "Heads", "Tails", "Heads", "Tails",   "Heads", "Tails", "Heads", "Tails", "It managed to land on it's side. :thinking:"]
  
    msg = await ctx.reply(":coin: | *Flipping...*")

    await asyncio.sleep(1)
  
    await msg.edit(content=random.choice(result))

  @commands.command(brief="Roll a die (yes that is the right word)", description="Rolls a die (and no, my grammar is not bad, that is the non-pluralated version of ''dice'''")
  async def d(self, ctx):
    result = ["1", "2", "3", "4", "5", "6"]
  
    msg = await ctx.reply(":game_die: |   *Rolling...*")
  
    await asyncio.sleep(1)
  
    await msg.edit(content=random.choice(result))

  @commands.command(brief="Yoink someone's info", description="Use this command to hack someone!\nAlso if you think this is real, you might want to do an IQ test.")
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def hack(self, message, member:discord.Member   = None):
    hack_amt = 5
  
    if member == None:
      await message.reply("We need to think of **who** we're hacking.")
  
    if member == self.client.user:
      await message.reply("As good of a try as that was, I'm not going to hack myself.\nHowever, I'm now going to hack **you**!")
      member = message.author
  
      await asyncio.sleep(3.5)
  
  
    message = await message.reply("**It's info   yoinking time!**\nHacking "+member.name)
  
    await asyncio.sleep(3)
  
    await message.edit(content=f"**1/{hack_amt}** | Finding e-mail address...")
  
    await asyncio.sleep(3)
  
    await message.edit(content=f"**1/{hack_amt}** | E-mail address found: `"+member.name  +"@discord.com`")
  
    await asyncio.sleep(2)
  
    await message.edit(content=f"**2/{hack_amt}** | Finding password to Discord Account...")
  
    await asyncio.sleep(3)
  
    await message.edit(content=f"**2/{hack_amt}** | Discord Account password found: `me("+member.name+")iscool"+member.discriminator+"`")
  
    await asyncio.sleep(2)
  
    await message.edit(content=f"**3/{hack_amt}** | Logging into Discord Account...")
  
    await asyncio.sleep(3)
  
    await message.edit(content=f"**3/{hack_amt}** | Logged in! Sending `leave.server` API requests...")
  
    await asyncio.sleep(3)
  
    server_number = random.randint(3,200)
    await message.edit(content=f"**3/{hack_amt}** | Made user leave {server_number} servers.")
  
    await asyncio.sleep(2)
  
    await message.edit(content=f"**4/{hack_amt}** | Checking user's Nitro History...")
  
    await asyncio.sleep(3)
  
    amount_spent = random.randint(4,199)
    amount_of_nitro_gifts = random.randint(1,15)
    history_choices = [f"Wow, £{amount_spent} spent on Nitro...", f"Wow, {amount_of_nitro_gifts} Nitro Gifts..."]
    history = random.choice(history_choices)
  
    await message.edit(content=f"**4/{hack_amt}** | {history}")
  
    await asyncio.sleep(2)
  
    await message.edit(content="*daydreaming*")
    
    await asyncio.sleep(0.25)
  
    await message.edit(content="oh yea, back to   hacking")
  
    await asyncio.sleep(1.2550)
  
    error_number = random.randint(1000,9999)
    embed = discord.Embed(title=f"ERROR #{error_number}  ",   description="ERROR.DISCORD_THIS_IS_NOT_A_REAL_HACK"  , color=0xff0000)
  
    await message.edit(content=f"Wait, what's this   error?! Did I drool on the keyboard?!",   embed=embed)
  
  
    await asyncio.sleep(3)
  
    await message.edit(content="Aw, looks like we're not hacking anyone after all. :frowning:")
  
  
    await asyncio.sleep(10)
  
    await message.delete()

  @commands.command(brief="!txet ruoy sesreveR", description="Reverses your text!")
  async def reverse(self, ctx, *, message):
    if message == None:
      message = "This is an example, because you didn't give me a message to reverse."

    await ctx.reply(message[::-1])





def setup(client):
    client.add_cog(Games(client))

print("games.py fully loaded")