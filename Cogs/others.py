import discord
import asyncio
import random
import psutil
import datetime, time
import randfacts
from discord.ext import commands
from dateutil.relativedelta import relativedelta
from discord_components import *

global startTime
startTime = time.time()


DiscordComponents(client)

buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]

def calculate(exp):
      o = exp.replace('×', '*')
      o = o.replace('÷', '/')
      result = ''
      try:
          result = str(eval(o))
      except:
          result = 'An error occurred.'
      return result

class Others(commands.Cog):
  def __init__(self, client):
    self.client = client

  #calculates answer
   
  @commands.command()
  async def calc(self, ctx):
      m = await ctx.send(content='Loading   Calculators...')
      expression = 'None'
      delta = datetime.datetime.utcnow() +   datetime.timedelta(minutes=5)
      e = discord.Embed(title=f'{ctx.author.name}\'s   calculator | {ctx.author.id}',   description=expression,
                          timestamp=delta)
      await m.edit(components=buttons, embed=e)
      while m.created_at < delta:
          res = await commands.wait_for('button_click')
          if res.author.id == int(res.message.embeds[0]  .title.split('|')[1]) and res.message.embeds[
              0].timestamp < delta:
              expression = res.message.embeds[0]  .description
              if expression == 'None' or expression ==   'An error occurred.':
                  expression = ''
              if res.component.label == 'Exit':
                  await res.respond  (content='Calculator Closed', type=7)
                  await asyncio.sleep(5)
                  await m.delete()
                  break
              elif res.component.label == '←':
                  expression = expression[:-1]
              elif res.component.label == 'Clear':
                  expression = 'None'
              elif res.component.label == '=':
                  expression = calculate(expression)
              else:
                  expression += res.component.label
              f = discord.Embed(title=f'  {res.author.name}\'s calculator | {res.author.id}', description=expression,
                                  timestamp=delta)
              await res.respond(content='', embed=f,   components=buttons, type=7)

  @commands.command()
  @commands.cooldown(3, 30, commands.BucketType.guild)
  async def fact(self, ctx):
    fact = randfacts.get_fact()
  
    await ctx.send(fact)


  @commands.command()
  async def rickroll(self, ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"mp3.mp3"))
    await ctx.author.send("Use that file to rickroll someone ;)")

  @commands.command(brief="FREE NITRO", description="Upon executing this command, the bot will give you a free Discord Nitro code in DMs!")
  async def gimmenitro(self, ctx):
    await ctx.author.send("||** **                        No                        ** **||")

  @commands.command(brief="Chooses a random number from a given range.", description="Using the range between the two numbers you give to the me, I will choose a random number. As long as the second number is bigger than the first number, then it can be any word, but please don't try to break me 😅", aliases=["randrange", "givenumber", "randomnumberfromrange"])
  async def randomnumber(self, ctx):
  
      def check(msg):
          return msg.author == ctx.author and   msg.content.isdigit() and \
                 msg.channel == ctx.channel
  
      await ctx.send("Type a number")
      msg1 = await commands.wait_for("message",   check=check)
      await ctx.send("Type a second, larger number")
      msg2 = await commands.wait_for("message",   check=check)
      x = int(msg1.content)
      y = int(msg2.content)
      if x < y:
          value = random.randint(x,y)
          await ctx.send(f"You got {value}.")
      else:
          await ctx.send(":warning: Please ensure the   first number is smaller than the second   number.")

  @commands.command(brief="Give someone a comforting hug!", description="Give someone a comforting hug!")
  async def hug(self, ctx, member : discord.Member):
    if member == None:
      member = ctx.author
  
    await ctx.reply(ctx.author.mention+" wrapped "  +member.mention+" in a warm hug!   <:BS_PandaLove:828739025526980629>")

  @commands.command(brief="Show bot latency", description="Show bot latency", aliases=["uptime"])
  async def ping(self, ctx):
    uptime = str(datetime.timedelta(seconds=int(round  (time.time()-startTime))))

    message = await ctx.reply(
      "**Pinging, this should be instant. If not, then I may be a bit busy.**",
    )


    await message.edit(content=f"```ansi\ndiscord:~> neofetch ~> discord/servers/758732319560826912-A-Blended-Server\n[0;34m⠀⠀⠀⠀⢀⣀⣤⣤⡀⠀⠀⠀⠀⢀⣤⣤⣀⡀⠀⠀⠀⠀   Discord[0m\n[0;34m⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀  [0m------------------\n[0;34m⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀  OS[0m: Discord App\n[0;34m⢀⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⡀  Uptime[0m: {uptime}\n[0;34m⣸⣿⣿⣿⣿⡏⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⢹⣿⣿⣿⣿⣇   Ping[0m: {round(self.client.latency * 1000)} ms\n[0;34m⣿⣿⣿⣿⣿⣧⡀⠀⣀⣾⣿⣿⣷⣀⠀⢀⣼⣿⣿⣿⣿⣿  Theme[0m: dark\n[0;34m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  Terminal[0m: code block\n[0;34m⠙⠻⢿⣿⣿⣶⡭⠙⠛⠛⠛⠛⠛⠛⠋⢭⣶⣿⣿⡿⠟⠋  [0m\n[0;34m⠀⠀⠀⠈⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⠁⠀⠀⠀    [0;30m███[0;31m███[0;32m███[0;34m███[0;35m███[0;36m███[0;37m███\n```\n(For those on mobile: Uptime: {uptime}, Ping: {round(self.client.latency * 1000)})")


#    await message.edit(content=f"Uptime: {uptime}\nPing: {round(self.client.latency * 1000)}")
    
    
  @commands.command()
  async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(f"{message}" .format(message))

  @commands.command(aliases=["useravatar", "getavatar", "getuseravatar", "fetchavatar", "fetchuseravatar", "showuseravatar"])
  async def avatar(self, ctx,*,member: discord.Member=None):
    if member == None:
      member = ctx.author
  
    memberavatar = member.avatar_url
  
    embed = discord.Embed(title=f"{member}'s Avatar",   color=0x008080)
    embed.set_image(url=memberavatar)
  
    await ctx.send(embed=embed)

  @commands.command()
  async def createfile(self, ctx, *, message):
    messagefile = open(f'Files by CMDs/{ctx.author.name}-message.txt', 'w')
    messagefile.write(message)
    messagefile.close()
    with open(f'Files by CMDs/{ctx.author.name}-message.txt', 'r') as file:

        await ctx.reply(f"{ctx.author.mention}\nHere is your file.\nThis message will automatically delete in 2.5 minutes.", file=discord.File(file, f'{ctx.author.name}-message.txt'), delete_after=150)




def setup(client):
    client.add_cog(Others(client))

print("others.py fully loaded")