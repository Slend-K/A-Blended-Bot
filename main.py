import discord
import os
import asyncio
import datetime, time
import randfacts
from keep_alive import keep_alive
from discord.ext import commands, tasks
from discord.ext import *
from discord_components import *
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
"""
slurs = [
    " 4r5e ",
    " 5h1t",
    " 5hit",
    " a55",
    " anal",
    " ar5e",
    " arrse",
    " arse",
    " ass ",
    " ass-fucker",
    " asses",
    " assfucker",
    " assfukka",
    " asshole",
    " assholes",
    " asswhole",
    " a_s_s",
    " b!tch",
    " b00bs",
    " b17ch",
    " b1tch",
    " ballbag",
    " balls",
    " ballsack",
    " bastard",
    " beastial",
    " beastiality",
    " bellend",
    " bestial",
    " bestiality",
    " bi+ch",
    " biatch",
    "bitch",
    "bitcher",
    "bitchers",
    "bitches",
    "bitchin",
    "bitching",
    "bloody",
    "blow job",
    "blowjob",
    "blowjobs",
    "boiolas",
    "bollock",
    "bollok",
    "boner",
    "boob",
    "boobs",
    "booobs",
    "boooobs",
    "booooobs",
    "booooooobs",
    "breasts",
    "buceta",
    "bunny fucker",
    "buttmuch",
    "buttplug",
    "c0ck",
    "c0cksucker",
    "carpet muncher",
    "cawk",
    "chink",
    "cipa",
    "cl1t",
    "clit",
    "clitoris",
    "clits",
    "cnut",
    "cock",
    "cock-sucker",
    "cockface",
    "cockhead",
    "cockmunch",
    "cockmuncher",
    "cocks",
    "cocksuck",
    "cocksucked",
    "cocksucker",
    "cocksucking",
    "cocksucks",
    "cocksuka",
    "cocksukka",
    "cok",
    "cokmuncher",
    "coksucka",
    "coon",
    "cox",
    "crap",
    "cum",
    "cummer",
    "cumming",
    "cums",
    "cumshot",
    "cunilingus",
    "cunillingus",
    "cunnilingus",
    "cunt",
    "cuntlick",
    "cuntlicker",
    "cuntlicking",
    "cunts",
    "cyalis",
    "cyberfuc",
    "cyberfuck",
    "cyberfucked",
    "cyberfucker",
    "cyberfuckers",
    "cyberfucking",
    "d1ck",
    "damn",
    "dick",
    "dickhead",
    "dildo",
    "dildos",
    "dink",
    "dinks",
    "dirsa",
    "dlck",
    "dog-fucker",
    "doggin",
    "dogging",
    "donkeyribber",
    "dyke",
    "ejaculate",
    "ejaculated",
    "ejaculates",
    "ejaculating",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "f u c k",
    "f u c k e r",
    "f4nny",
    "fag",
    "fagging",
    "faggitt",
    "faggot",
    "faggs",
    "fagot",
    "fagots",
    "fags",
    "fanny",
    "fannyflaps",
    "fannyfucker",
    "fanyy",
    "fatass",
    "fcuk",
    "fcuker",
    "fcuking",
    "feck",
    "fecker",
    "felching",
    "fellate",
    "fellatio",
    "fingerfuck",
    "fingerfucked",
    "fingerfucker",
    "fingerfuckers",
    "fingerfucking",
    "fingerfucks",
    "fistfuck",
    "fistfucked",
    "fistfucker",
    "fistfuckers",
    "fistfucking",
    "fistfuckings",
    "fistfucks",
    "flange",
    "fook",
    "fooker",
    "fuck",
    "fucka",
    "fucked",
    "fucker",
    "fuckers",
    "fuckhead",
    "fuckheads",
    "fuckin",
    "fucking",
    "fuckings",
    "fuckingshitmotherfucker",
    "fuckme",
    "fucks",
    "fuckwhit",
    "fuckwit",
    "fudge packer",
    "fudgepacker",
    "fuk",
    "fuker",
    "fukker",
    "fukkin",
    "fuks",
    "fukwhit",
    "fukwit",
    "fux",
    "fux0r",
    "f_u_c_k",
    "gangbang",
    "gangbanged",
    "gangbangs",
    "gaylord",
    "gaysex",
    "goatse",
    "god",
    "god-dam",
    "god-damned",
    "goddamn",
    "goddamned",
    "hardcoresex",
    "hell",
    "heshe",
    "hoar",
    "hoare",
    "hoer",
    "homo",
    "hore",
    "horniest",
    "horny",
    "hotsex",
    "jack-off",
    "jackoff",
    "jap",
    "jerk-off",
    "jism",
    "jiz",
    "jizm",
    "jizz",
    "kawk",
    "knob",
    "knobead",
    "knobed",
    "knobend",
    "knobhead",
    "knobjocky",
    "knobjokey",
    "kock",
    "kondum",
    "kondums",
    "kum",
    "kummer",
    "kumming",
    "kums",
    "kunilingus",
    "l3i+ch",
    "l3itch",
    "labia",
    "lust",
    "lusting",
    "m0f0",
    "m0fo",
    "m45terbate",
    "ma5terb8",
    "ma5terbate",
    "masochist",
    "master-bate",
    "masterb8",
    "masterbat*",
    "masterbat3",
    "masterbate",
    "masterbation",
    "masterbations",
    "masturbate",
    "mo-fo",
    "mof0",
    "mofo",
    "mothafuck",
    "mothafucka",
    "mothafuckas",
    "mothafuckaz",
    "mothafucked",
    "mothafucker",
    "mothafuckers",
    "mothafuckin",
    "mothafucking",
    "mothafuckings",
    "mothafucks",
    "mother fucker",
    "motherfuck",
    "motherfucked",
    "motherfucker",
    "motherfuckers",
    "motherfuckin",
    "motherfucking",
    "motherfuckings",
    "motherfuckka",
    "motherfucks",
    "muff",
    "mutha",
    "muthafecker",
    "muthafuckker",
    "muther",
    "mutherfucker",
    "n1gga",
    "n1gger",
    "nazi",
    "nigg3r",
    "nigg4h",
    "nigga",
    "niggah",
    "niggas",
    "niggaz",
    "nigger",
    "niggers",
    "nob",
    "nob jokey",
    "nobhead",
    "nobjocky",
    "nobjokey",
    "numbnuts",
    "nutsack",
    "orgasim",
    "orgasims",
    "orgasm",
    "orgasms",
    "p0rn",
    "pawn",
    "pecker",
    "penis",
    "penisfucker",
    "phonesex",
    "phuck",
    "phuk",
    "phuked",
    "phuking",
    "phukked",
    "phukking",
    "phuks",
    "phuq",
    "pigfucker",
    "pimpis",
    "piss",
    "pissed",
    "pisser",
    "pissers",
    "pisses",
    "pissflaps",
    "pissin",
    "pissing",
    "pissoff",
    "poop",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "prick",
    "pricks",
    "pron",
    "pube",
    "pusse",
    "pussi",
    "pussies",
    "pussy",
    "pussys",
    "rectum",
    "retard",
    "rimjaw",
    "rimming",
    "s hit",
    "s.o.b.",
    "sadist",
    "schlong",
    "screwing",
    "scroat",
    "scrote",
    "scrotum",
    "semen",
    "sex",
    "sh!+",
    "sh!t",
    "sh1t",
    "shag",
    "shagger",
    "shaggin",
    "shagging",
    "shi+",
    "shit",
    "shitdick",
    "shite",
    "shited",
    "shitey",
    "shitfuck",
    "shitfull",
    "shithead",
    "shiting",
    "shitings",
    "shits",
    "shitted",
    "shitter",
    "shitters",
    "shitting",
    "shittings",
    "shitty",
    "skank",
    "slut",
    "sluts",
    "smegma",
    "smut",
    "snatch",
    "son-of-a-bitch",
    "spac",
    "spunk",
    "s_h_i_t",
    "t1tt1e5",
    "t1tties",
    "teets",
    "teez",
    "testical",
    "testicle",
    "tit",
    "titfuck",
    "tits",
    "titt",
    "tittie5",
    "tittiefucker",
    "titties",
    "tittyfuck",
    "tittywank",
    "titwank",
    "tosser",
    "turd",
    "tw4t",
    "twat",
    "twathead",
    "twatty",
    "twunt",
    "twunter",
    "v14gra",
    "v1gra",
    "vagina",
    "viagra",
    "vulva",
    "w00se",
    "wang",
    "wank",
    "wanker",
    "wanky",
    "whoar",
    "whore",
    "willies",
    "willy",
]
"""
'''
time_regex = re.compile("(?:(\d{1, 5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

async def TimeConverter(ctx, argument):
  args = argument.lower()
  matches = re.findall(time_regext, args)
  time = 0
  for key, value in matches:
    try:
      time += time_dict[value] * float(key)
    except KeyError:
      raise commands.BadArgument(f"{value} is an invalid time unit! `d`, `h`, `m`, `s` are valid arguments")
    except ValueError:
      raise commands.BadArgument(f"{key} is not a number!")
  return round(time)

'''
client = discord.Client()

intents=discord.Intents.all()
client = commands.Bot(command_prefix="b.", case_insensitive=True, intents=intents)

@client.event
async def on_ready():
  print("Bot is ready to rumble!")
  for filename in os.listdir(f"./Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")


  global startTime
  startTime = time.time()

  # MAINTENENCE STATUS;
  # UNCOMMENT THIS AND TRIPLE-QUOTE COMMENT THE LOOP
  '''
  await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=5, name="PYTHON | DOWN FOR MAINTENANCE"))
  '''


client.load_extension("jishaku")
print("Jishaku has been loaded.")




@client.event
async def on_message(ctx):
  messageattachments = ctx.attachments
  if len(messageattachments) > 0:
    for attachment in messageattachments:
                if attachment.filename.endswith(".dll"):
                    await ctx.delete()
                    await ctx.channel.send(f"Sorry {ctx.author.mention}, files of the following types `.dll`, `.exe`, `.vbs` and `.bat` are not allowed, as they can cause damage to someone's PC")
                elif attachment.filename.endswith('.exe'):
                    await ctx.delete()
                    await ctx.channel.send(f"Sorry {ctx.author.mention}, files of the following types `.dll`, `.exe`, `.vbs` and `.bat` are not allowed, as they can cause damage to someone's PC")
                elif attachment.filename.endswith(".vbs"):
                  await ctx.delete()
                  await ctx.channel.send(f"Sorry {ctx.author.mention}, files of the following types `.dll`, `.exe`, `.vbs` and `.bat` are not allowed, as they can cause damage to someone's PC")
                elif attachment.filename.endswith(".bat"):
                  await ctx.delete()
                  await ctx.channel.send(f"Sorry {ctx.author.mention}, files of the following types `.dll`, `.exe`, `.vbs` and `.bat` are not allowed, as they can cause damage to someone's PC")

                else:
                    break
                    
  if ctx.content.startswith("c."):
    badprefix = await ctx.reply("I assume you were trying to trigger me.\nMy new prefix is `b.`, to suit the new name of the server.")

    await asyncio.sleep(8)
    await ctx.delete()
    await badprefix.delete()
  """
  for word in slurs:
    if word in ctx.content.lower():
      print(f"\nI spotted a bad word.\nMessage content: {ctx.content}\nSender: {ctx.author.name}#{ctx.author.discriminator} | {ctx.author.id}")
      
      await ctx.reply("Hey, we're a family-friendly server and you can't say that.")
      
      await ctx.delete()
      print("I deleted it.")

      channel = client.get_channel(758784153063260170)

      embed = discord.Embed(title=f"{ctx.author.name} said a bad word.", description="I deleted it.", color=discord.Color.red())
      embed.add_field(name="Content:", value=ctx.content)
      embed.add_field(name="User Information", value=f"{ctx.author.name}#{ctx.author.discriminator} | {ctx.author.id}")

      await channel.send(embed=embed)
  """
  await client.process_commands(ctx)

@client.event
async def on_member_join(member):
  print("\nNew member joined! Welcoming...\n")
  channel = client.get_channel(758732856222154826)

  pfp = member.avatar_url_as(size=256)
  data = BytesIO(await pfp.read())
  pfp = Image.open(data)

  pfp = pfp.resize((425, 425))

  img = Image.open("bot welcome image.png")

  font = ImageFont.truetype("PixAntiqua.ttf", 130)

  draw = ImageDraw.Draw(img)

  #draw.line(((955, 811), (200, 100)), "gray")
  #draw.line(((811, 955), (100, 200)), "gray")
  draw.text((955, 825), f"{member.name}#{member.discriminator}", fill="orange",   anchor="mm", font=font)

  img.paste(pfp, (750, 290))

  img.save("personalised bot welcome image.png")

  await channel.send(f"\n\n**{member.name}** just hopped into the Blender!\n{member.name} joined at {datetime.datetime.now()}", file=discord.File("personalised bot welcome image.png"))

  print("I have finished welcoming the new member.")
  print(f"Name: {member.name}\nDiscriminator: #{member.discriminator}\nID: {member.id}\nFull username: {member.name}#{member.discriminator} | {member.id}")

  logs = client.get_channel(758784153063260170)

  logsembed = discord.Embed(title="New Member's Information", description=f"Name: {member.name}\nDiscriminator: #{member.discriminator}\nID: {member.id}\n@ Mention: {member.mention}\nFull username: {member.name}#{member.discriminator} | {member.id}", color=discord.Color.random())
  logsembed.set_thumbnail(url=member.avatar_url)
  
  await logs.send("New member joined!", embed=logsembed)

  print("Waiting to ensure I get updated results for when I update the channel.")

  await asyncio.sleep(3)

  print("Wait over;")

  print("Editing the membercount channel...")

  abs = client.get_guild(758732319560826912)
  
  all_members = client.get_channel(950854412966981712)
  bots = client.get_channel(950857713125032016)
  humans = client.get_channel(950857751041540196)

  
  # BOT COUNT
  members = abs.members
  bot_count = 0
  for i in members:
        member = i.bot
        if member == True:
            bot_count += 1

  human_count = abs.member_count - bot_count

  await all_members.edit(name=f"All Members: {abs.member_count}")

  await bots.edit(name=f"Bots: {bot_count}")

  await humans.edit(name=f"Humans: {human_count}")



@client.event
async def on_member_remove(member):
  channel = client.get_channel(758732856222154826)

  await channel.send(f"{member.name}#{member.discriminator} has left A Blended Server.")

  print(f"\n{member.name}#{member.discriminator} has left A Blended Server.\n")

  print("Waiting to ensure I get updated results for when I update the channel.")

  await asyncio.sleep(3)

  print("Wait over;")

  print("Editing the membercount channel...")

  abs = client.get_guild(758732319560826912)
  
  all_members = client.get_channel(950854412966981712)
  bots = client.get_channel(950857713125032016)
  humans = client.get_channel(950857751041540196)

  
  # BOT COUNT
  members = abs.members
  bot_count = 0
  for i in members:
        member = i.bot
        if member == True:
            bot_count += 1

  human_count = abs.member_count - bot_count

  await all_members.edit(name=f"All Members: {abs.member_count}")

  await bots.edit(name=f"Bots: {bot_count}")

  await humans.edit(name=f"Humans: {human_count}")


# ERROR HANDLERS



@client.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send("You do not have permission to run that command.")

  elif isinstance(error,commands.MissingRequiredArgument):
    embedVar = discord.Embed(title="Oops, you're missing something!", description="You're missing an argument or two. Make sure you enter them all and enter them correctly.\n\nYou're likely missing a member's name or ID.\nIf it's not that, but you're still not sure what you're missing, try running `c.help {command}`.", color=0xff0000)

    await ctx.send(embed=embedVar)


  elif isinstance(error, commands.CommandOnCooldown):
    embedVar = discord.Embed(title="Slow down! That command is on cooldown!", description="That command is on cooldown - you'll have to wait until cooldown is over.\n**UNIQUE COOLDOWN SYSTEMS**:\n`c.hack` has `30 seconds` of cooldown.\n`c.fact` has `30 seconds` of **global** cooldown for every `3` uses.", color=0xff0000)

    await ctx.send(embed=embedVar)

  elif isinstance(error,commands.MemberNotFound):
    await ctx.send("I could not find that user. Check if you made any mistakes.")

  elif isinstance(error,commands.NoPrivateMessage):
    await ctx.send("This command cannot be used in private messages.")
  elif isinstance(error,commands.CommandNotFound):
    msg = await ctx.reply("Oops, that's not a command that I could find.\nDid you get the wrong prefix, wrong spelling or just didn't mean to do this?")

    await asyncio.sleep(3)
    await ctx.message.delete()
    await msg.delete()

  else:
    raise error

# ░█████╗░███╗░░░███╗██████╗░░██████╗
# ██╔══██╗████╗░████║██╔══██╗██╔════╝
# ██║░░╚═╝██╔████╔██║██║░░██║╚█████╗░
# ██║░░██╗██║╚██╔╝██║██║░░██║░╚═══██╗
# ╚█████╔╝██║░╚═╝░██║██████╔╝██████╔╝
# ░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░


# Put all commands either in their respective cogs
# or ABOVE these loops.

'''
FACT(S) OF THE DAY LOOP
'''
@tasks.loop(hours=24)
async def called_once_every_day():
    message_channel = client.get_channel(790679757154680863)
    print(f"Got channel {message_channel}")
    await message_channel.send(f"{randfacts.get_fact()}")

@called_once_every_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_every_day.start()


'''
STATUS LOOP
'''
"""
async def ch_pr():
    await client.wait_until_ready()

    members = 0
    for guild in client.guilds:
      members += guild.member_count - 1

    facts = randfacts.get_fact()

    statuses = [f"over all {members} of you in the Blended Server", "Slend_K's Twitch Streams", "Slender the Blender's YouTube Videos", f"DID YOU KNOW: {facts}"]

    while not client.is_closed():

      status = random.choice(statuses)

      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

      await asyncio.sleep(120)

client.loop.create_task(ch_pr())
"""

# Run

if __name__ == '__main__':
  keep_alive()
  client.run(os.getenv("TOKEN"))

print("main.py fully loaded.")