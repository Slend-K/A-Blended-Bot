import discord
import asyncio
import random
from discord.ext import commands, tasks
from discord.ext import *
from discord.ext.commands import cooldown, BucketType
from discord_components import *


class Server(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def suggest(self, ctx, *,message):
    await ctx.send(f"Thank you, {ctx.author.mention},   your suggestion has been sent to   <#764171893908439102>!")
  
  
    channel = self.client.get_channel(764171893908439102) 
  
    embedVar = discord.Embed(title="New suggestion!", description=f"{message}", color=0x27db91)
    embedVar.set_footer(text="Submitted by: {}".format  (ctx.author.display_name),   icon_url=ctx.author.avatar_url)
  
  
    m = await channel.send(embed=embedVar)
  
    await m.add_reaction("👍")
    await m.add_reaction("👎")

  @commands.command()
  async def anonsuggest(self, ctx, *,message):
    await ctx.send("Thank you, "+ctx.author.mention+ ", your suggestion has been sent to <#764171893908439102>!")
  
  
    channel = self.client.get_channel(764171893908439102) 
  
    embedVar = discord.Embed(title="New suggestion!",   description=f"{message}", color=0x27db91)
    embedVar.set_footer(text="This suggestion was   submitted anonymously.")
  
    m = await channel.send(embed=embedVar)
  
    await m.add_reaction("👍")
    await m.add_reaction("👎")

  @commands.command(brief="Bot/Server information", description="This command will bring a short embed giving information on either the bot or server.")
  async def info(self, ctx):
  
    embed = discord.Embed(title="Information - Bot",   description="I am a bot made for and only for   the Blended Server. My main purpose is just to add a bit   more to the Blended Server, in the form of fun commands.   Find them with `c.help`.\nI was originally made   with [Botghost](https://botghost.com/), but now I   am completely coded by <@!665641503376539669>.",   color=0xcbf835)
    embed.add_field(name="Creation Date",   value="20/10/2020", inline=True)
    embed.add_field(name="Code information",   value="Language: Python\n   - Python v3.8\nIDLE:   Replit.", inline=True)
    embed.add_field(name="Ping", value=f"My ping is `  {round(commands.latency * 1000)}ms`")
        
    await ctx.reply(embed=embed)

  format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

  @commands.command()
  @commands.guild_only()
  async def serverinfo(self, ctx):
    embed = discord.Embed(
        color = ctx.guild.owner.top_role.color
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}**\n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def refresh_server_count_channel(self, ctx):
    print("Refreshing & the membercount channel...")

    abs = self.client.get_guild(758732319560826912)
  
    all_members = self.client.get_channel(950854412966981712)
    bots = self.client.get_channel(950857713125032016)
    humans = self.client.get_channel(950857751041540196)

  
    # BOT COUNT
    members = abs.members
    bot_count = 0
    for i in members:
        member = i.bot
        if member == True:
            bot_count += 1

    human_count = abs.member_count - bot_count

    await all_members.edit(name=f"All Members: {abs.member_count}")
    await ctx.reply(f"Refreshed {all_members.mention}.")

    await bots.edit(name=f"Bots: {bot_count}")
    await ctx.send(f"Refreshed {bots.mention}")

    await humans.edit(name=f"Humans: {human_count}")
    await ctx.send(f"Refreshed {humans.mention}")

    print(f"Channels Refreshed\nEdited: {all_members.id}, {bots.id}, {humans.id}")

    

  @commands.command(brief="Good ol' chat reviver!", description="Wheter this is to just change the topic, or to revive the chat, this command has you covered!")
  async def topic(self, ctx):
    list_of_responses = ["What's your favourite place   to visit?",
  
    "Where is the last place you went on holiday?",
  
    "If you were given £1,000,000 (or whatever   currency you use), what would you buy?",
  
    "Do you prefer big trucks or small family cars?",
  
    "What's your dream car?",
  
    "What's your dream job?",
  
    "Do you prefer the hot or cold? Or is your   favourite a little bit in the middle?",
  
    "Are you a speaker or a silent one?",
  
    "What's your favourite game?",
  
    "What's your favourite sport?",
  
    "If you could only eat one thing for the rest of   your life, what would it be?",
  
    "What's your biggest fear?",
  
    "Have you ever had a NDE (**N**ear **D**eath   **E**xperiance)? It's ok if you'd rather not   share!",
  
    "If you became King/Queen/President for 1 week,   what would you do?",
  
    "If the Earth only had 24 hours before it ended,   what would you do for the remaining time?",
  
    "What is your favourite Discord bot? Mind sharing   why?",
  
    "What would you do if you had Discord Nitro   (Regular)? Would you start using the perks   instantly, or would you treat it like you haven't   got it, only using them when you need them.",
  
    "Even if you were given £1,000,000, what is   something you still wouldn't do?",
  
    "What would you do only if you were given £1,000,  000?",
  
    "What is your opinion on light mode? (Any light   mode, not just Discord's)",
  
    "What's your favourite thing about the Blended Server?",
  
    "What's your favourite thing about Discord?",
  
    "What's your least favourite thing about Discord?",
  
    "How are you doing today?",
  
    "** <:BS_monkaw:790663861745090600> YOUR PHONE   MIGHT BE LOW ON CHARGE! CHARGE IT!   <:BS_monkaw:790663861745090600> **",
  
    "What is not in your fridge, but should have been   in there? Make sure nothing goes bad and makes you   ill! (Credit to KoelKast for this question.)",
  
    "What is your favourite video game?",
  
    "What's your favourite game franchise?",
  
    "** <:monkaX:790663861769338910> YOUR LAPTOP MIGHT   BE LOW ON CHARGE! C H A R G E    I T!   <:monkaX:790663861769338910> **",
  
    "Can we get some hype for those awesome people who   do things to make the world a better place?   <:monkaHype:801174902816243772>",
  
    "If you could make one country, what would it be   called?\n What language would they speak?\n Would   you make one up?\n What would the currency be?\n   What would the currency be worth VS your local   currency? \nSo many questions!   <:BS_monkaw:790663861745090600>",
  
    "Do you still remember the rules? :thinking: Have   a double-check of them :wink:",
  
    "Can we get some hype in the chat for our awesome   moderators?!\n <:monkaHype:801174902816243772>",
  
    "If you could invent one thing, what would it be?   What would it do? How much would it cost?",
  
    "Who is the most famous person you have met?",
  
    "hi",
  
    "If you could change one thing in the world, what   would you change?",
  
    "If you could meet any celebrity, who would it be?  ",
  
    "If you could turn into one celebrity, who would   it be?",
  
    "What Discord Client are you using? (e.g Canary,   Normal, PTB, etc.)",
  
    "Do you know how to activate Discord's   Android-Only Ultra Light and Dark modes?",
  
    "What would you rate Discord out of 10?",
  
    "What would you rate the Blended Server out of 10?",
  
    "What is your favourite food?",
  
    "What is your favourite dog bread?",
  
    "What is your favourite cat breed?",
  
    "What is your favourite animal?",
  
    "Do you have any pets?",
  
    "What is your most favourite movie?",
  
    "What is your least favourite movie?",
  
    "What is your most favourite TV show?",
  
    "What is the biggest risk you've ever taken?",
  
    "What is your favourite emote that has been added   to the Blended Server? Slend's favourite is either:   <:BS_KEKW:790663862026240001> ,   <:BS_monkaX:790663861769338910> ,   <:BS_PagChomp:790663862868639795> or   <:BS_shut:790663862571237437> . As you can see, he   is indecisive.",
  
    "What is your favourite song?",
  
    "What is your least favourite song?",
  
    "What would you do differently if you could relive   the past year?",
  
    "If you knew that you only had a year left to live,   what would you do?",
  
    "If you could choose to have one superpower, what   would it be? Would you use it to be evil, a hero   or use it for it to be advantageous to just you?",
  
    "Would you rather be a superhero or a supervillian?  ",
  
    "What is something you have for breakfast everyday?  ",
  
    "What is your favourite drink?",
  
    "Would you rather: Sit all day **__OR__** Stand   all day",
  
    "Are you a pessimist or an optimist?",
  
    "What is your favourite shop?",
  
    "If anything you did had a **0% chance of   failure**, what would you do?",
  
    "What is your favourite thing to do on weekends?",
  
    "What is something cursed that should never be   said at a wedding?",
  
    "What is something that should never be said at a   funeral?",
  
    "What's something not many people know about you?",
  
    "What makes you laugh out loud?",
  
    "What's something not many people know about you?",
  
    "What is the worst advice you have given?",
  
    "What is the worst present you have ever received   and why?",
  
    "If you were a farm animal, which would you be and   why?",
  
    "Who’s your favorite comedian?",
  
    "If you could make up a school subject, what would   it be?",
  
    "If you had the opportunity to invent a new ice   cream flavor, what would it be?",
  
    "If you had a robot for the entire day, what would   you ask it to do?",
  
    "If you could be famous, would you want to? Why?",
  
    "If you had $100, what would you spend it on?",
  
    "If you had $500,000, what would you spend it on?",
  
    "What are the top three things on your bucket list?   It's OK if you'd rather not share!",
  
    "What is the biggest risk you’ve ever taken?",
  
    "**__DEEP QUESTION ALERT__** If someone gave you   an envelope with your death date inside of it,   would you open it?",
  
    "What is your idea of the perfect day?",
  
    "Who has been the most influential person in your   life and why?",
  
    "Do you think your priorities have changed since   you were younger?",
  
    "What scares you most about your future?",
  
    "What is the best or worst trait you inherited   from your parents?",
  
    "What motivates you most in life?",
  
    "Are you a cat person or a dog person?",
  
    "**__DEEP-ISH QUESTION ALERT__** When you die,   what do you want to be reincarnated as?",
  
    "Would you rather be invisible or have X-ray   vision?",
  
    "If you could only save one item from a house fire   (pets and family are already saved), what would it   be?",
  
    "What time period would you travel to?",
  
    "What’s the nicest thing a family member has ever   done for you?",
  
    "How long can you go without checking your phone?",
  
    "Have you ever really kept a New Year’s resolution?  ",
  
    "Can you tell when someone is lying?",
  
    "If someone offered to tell you your future, would   you accept it?",
  
    "If you were to remove one social media app from   your phone, which would it be and why?",
  
    "If you could have tea with a fictional character,   who would that be?",
  
    "If you were on death row, what would your last   meal be?",
  
    "What’s the weirdest dream you’ve ever had?",
  
    "What would you do if you were home alone and the   power went out?",
  
    "What made you laugh this week?",
  
    "If you could choose which sense you lose, what   would it be? Why?",
  
    "What is the craziest thing you have ever done?",
  
    "What is something that you've never done but   would like to try?",
  
    "Do you prefer to shop online or in a store?",
  
    "If you were the opposite gender for one day, what   would you do?",
  
    "What is your earliest memory?",
  
    "If you could choose any age to go back to, what   would you go back to? Why?",
  
    "If you could live anywhere on earth, where would   you live?",
  
    "What's the longest you have gone without sleep?",
  
    "What is the longest that you've stayed awake for?  ",
  
    "What would you want your last words to be?",
  
    "What was your worst restaurant experience?",
  
    "What is your favorite pizza topping?",
  
    "If you could acquire any skill, what would you   choose?",
  
    "If you were given three wishes, what would you   wish for?",
  
    "What is one thing that you can not live without?",
  
    "What is the favourite skill that you have?",
  
    "What phone do you have?",
  
    "If you were granted **__only one__** wish, what   would you wish for? *(Wishing for more wishes   isn't allowed)*",
  
    "Do you play any instruments?",
  
    "What do you like to do in your spare time?",
  
    "What is the first thing you do when you wake up?",
  
    "What is the last thing you do before you go to   sleep?",
  
    "What was your worst vacation experience?",
  
    "What countries have you traveled to?",
  
    "Where do you plan on going for your next vacation?  ",
  
    "What is your favorite restaurant?",
  
    "Are there any foods that you would like to try?",
  
    "Are there any foods that you dislike or will not   eat?",
  
    "What is your favorite meal of the day?",
  
    "What is your favorite ice cream flavor?",
  
    "Who is your favorite actor?",
  
    "What was the last movie you've seen?",
  
    "What type of music do you like to listen to?",
  
    "Who is your favorite music artist?",
  
    "What was the last book you read?",
  
    "Do you drink coffee or tea?",
  
    "If you were stranded on a deserted island and you   could have only 1 item, what would it be?",
  
    "Do you believe in luck?",
  
    "What is your favorite board game?",
  
    "Would you prefer to live in the city or a rural   area?",
  
    "Do you speak any other languages?",
  
    "Have you ever cried because you were so happy?   What made you this happy?",
  
    "What is your favourite computer font?",
                        
    "What would you spend if you had £1,000,000 **but could only spend it on __others__**?",
                        
    "What are your PC/laptop specs?"]
  
    await ctx.send(random.choice(list_of_responses))




def setup(client):
    client.add_cog(Server(client))

print("server.py fully loaded.")