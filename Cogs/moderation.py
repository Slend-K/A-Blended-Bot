import discord
import os
import asyncio
import json
import datetime, time
from discord.ext import commands, tasks
from discord.ext import *
from discord.ext.commands import cooldown, BucketType
from discord_components import *
from copy import deepcopy
import humanfriendly


class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(brief="Changes a user's nickname.", description="Changes someone's nickname to something you specify.")
  @commands.has_permissions(manage_nicknames=True)
  async def changenick(self, ctx, member: discord.Member,*, nick):
    if member == None:
      nope = await ctx.reply("You need to specify a user who's nickname you're going to remove.")
    
      await asyncio.sleep(5)
      await nope.delete()
      return
  
    if nick == None:
      nopenick = await ctx.reply("You need to specify a new nickname.")
  
      await asyncio.sleep(5)
      await nopenick.delete()
      return


    await member.edit(nick=nick)
    await ctx.reply("Done")

  @commands.command(aliases=["newnick"], description="Edit the nickname of a Member")
  async def setnick(self, ctx, member: discord.Member=None):
    if member == None:
      no_member = await ctx.reply("You need to tell me   who I'm changing the nickname of, either by   mentioning them or giving me their ID.")
  
      await asyncio.sleep(5)
      await no_member.delete()
      await ctx.message.delete()
  
    number = random.randrange(0, 100000)
    
    await member.edit(nick=f"Innap. Nick ¦ {number}")
    done = await ctx.reply(f"Done! ||{member.name}||'s   name is now {member.display_name}!")
  
    await asyncio.sleep(5)
    await done.delete()
    await ctx.message.delete()

  @commands.command(aliases=["k"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx,member: discord.Member,*,   reason="No reason provided"):
    if member == ctx.author:
      selfembed = discord.Embed(title="Error", description="You cannot kick yourself. That's probably not the best idea anyway.", color = discord.Color.red())
      await ctx.reply(embed=selfembed)

      selfmsg = await asyncio.sleep(5)
      await selfmsg.delete()
      await ctx.messsage.delete()

      return

    await member.kick(reason=reason)
  
    embed = discord.Embed(title="Memeber kicked!",   description=f"I kicked {member.name}#  {member.discriminator} for: **{reason}**.",   color=0xff0000)
    kick_confirmation = await ctx.reply(embed=embed)
  
    try:
      embed = discord.Embed(title="You were kicked   from A Blended Server.", description="** **")
      embed.add_field(name="Reason from moderator",   value=f"{reason}")
      
      await member.send(embed)
    except:
      cannot_dm = await ctx.send("I could not send a   DM to the user, as they likely had their DMs   closed.")
  
    
    channel = commands.get_channel(758784153063260170)
  
    embed = discord.Embed(title="Member kicked!",   description="", color=0xff0000)
    embed.add_field(name="Who was kicked?",   value=member.mention, inline = True)
    embed.add_field(name="Who kicked them?",   value=ctx.author.mention, inline=True)
    embed.add_field(name="What reason did the   moderator provide?", value=reason, inline=True)
  
    await channel.send(embed=embed)
  
    await asyncio.sleep(8)
  
    await kick_confirmation.delete()
    await cannot_dm.delete()
    await ctx.message.delete()

  @commands.command(aliases=["removenick"], description="Edit the nickname of a Member")
  async def nick(self, ctx, member: discord.Member=None):
    if member == None:
      no_member = await ctx.reply("You need to tell me who I'm changing the nickname of, either by mentioning them or giving me their ID.")
  
      await asyncio.sleep(5)
      await no_member.delete()
      await ctx.message.delete()
  
    number = random.randrange(0, 100000)
    
    await member.edit(nick=f"Innap. Nickname ¦ {number}")
    done = await ctx.reply(f"Done! ||{member.name}||'s name is now {member.display_name}!")
  
    await asyncio.sleep(5)
    await done.delete()
    await ctx.message.delete()

  @commands.command(aliases=["bigbop", "banish"])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx,member: discord.Member,*,   reason="No reason provided"):
    if member == ctx.author:
      selfembed = discord.Embed(title="Error", description="You cannot ban yourself. That's probably not the best idea anyway.", color = discord.Color.red())
      await ctx.reply(embed=selfembed)

      selfmsg = await asyncio.sleep(5)
      await selfmsg.delete()
      await ctx.messsage.delete()

      return

    await member.ban(reason=reason)
  
    embed = discord.Embed(title="Member Banned!",   description=f"I banned {member.name}#  {member.discriminator} for: **{reason}**",   color=0xff0000)
    ban_confirmation = await ctx.reply(embed=embed)
  
    try:
      embed = discord.Embed(title="You were banned   from A Blended Server.", description="** **")
      embed.add_field(name="Reason from moderator",   value=f"{reason}")
  
      await member.send(embed=embed)
    except:
      cannot_dm = await ctx.send("I could not DM the   user; they likely have their DMs closed.")
  
    channel = self.get_channel(758784153063260170)
  
    embedVar = discord.Embed(title="Member banned!",   description="", color=0xff0000)
    embedVar.add_field(name="Who was banned?",   value=member.mention, inline = True)
    embedVar.add_field(name="Who banned them?",   value=ctx.author.mention, inline=True)
    embedVar.add_field(name="What reason did the   moderator provide?", value=reason, inline=True)
  
    await channel.send(embed=embedVar)
  
    await asyncio.sleep(8)
  
    await ban_confirmation.delete()
    await cannot_dm.delete()

  @commands.command(aliases=["ub", "unbop"])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx,*,member):
    if member == ctx.author:
      selfembed = discord.Embed(title="Error", description="You can't unban yourself. If you were banned you wouldn't be able to unban yourself anyway...", color = discord.Color.red())
      await ctx.reply(embed=selfembed)

      selfmsg = await asyncio.sleep(5)
      await selfmsg.delete()
      await ctx.messsage.delete()

      return

    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")

    for banned_entry in banned_users:
      user = banned_entry.user

      if(user.name, user.discriminator)==(member_name, member_disc):

          await ctx.guild.unban(user)
 
          embedVar = discord.Embed(title="Member  Unbanned!", description="I have unbanned  the member!", color=0x0000ff)
          
          await ctx.send(embed=embedVar)
 
          channel = self.get_channel (830416385120534549)
 
          embedVar = discord.Embed(title="Member  unbanned!", description="", color=0xff0000)
          embedVar.add_field(name="Who was unbanned?",  value=member.mention, inline = True)
          embedVar.add_field(name="Who unbanned them? ", value=ctx.author.mention, inline=True)
 
          await channel.send(embed=embedVar)
 
          return

      await ctx.send(member+" was not found. Did you get the name right?")

  # WARNING SYSTEM
  # WARNING SYSTEM
  # WARNING SYSTEM

  @commands.command(brief="Warn a member", description="Warns a specified member with a specified reason.", aliases=["strike"])
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def warn(self, ctx, member: discord.Member, *, reason="Breaking the rules."):
    if member.id == ctx.author.id:
      selfmsg = await ctx.reply("You cannot warn yourself.")

      await asyncio.sleep(5)
      await selfmsg.delete()
      await ctx.message.delete()

      return

    if member.id == self.client.user.id:
      botmsg = await ctx.reply("no")
      await asyncio.sleep(0.5)
      await botmsg.edit(content="You cannot warn the hammer. **I  a m   t h e   h a m m e r**")

      await asyncio.sleep(5)
      await botmsg.delete()
      await ctx.message.delete()

      return

  @commands.command(aliases=["slowmode","setslowmode", "setsm", "sm"])
  @commands.has_permissions(manage_channels=True)
  async def setdelay(self ,ctx, seconds: int):
      await ctx.channel.edit(slowmode_delay=seconds)
      await ctx.reply(f"Set the slowmode delay in this channel to {seconds} seconds!")


  @commands.command(aliases=["delete", "del", "remove", "rem", "purge"])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=50+1):
    await ctx.channel.purge(limit = amount)

    done = await ctx.send(f"I have deleted those {amount} messages for you!")

    await asyncio.sleep(5)
    await done.delete()
  """
  @commands.command(brief="Timeout/tempmute someone", description="This command will timeout/tempmute a specified user with a specified reason.", aliases=["timeout", "tempmute"])
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, user: discord.Member, t_o_time="3h",*, reason="No reason specified."):
    if user == None:
      nouser = await ctx.reply("You didn't specify who I am tempmuting.")

      await asyncio.sleep(5)
      await nouser.delete()
      await ctx.message.delete()

    time = humanfriendly.parse_timespan(t_o_time)

    await user.timeout(time, reason=reason)

    await ctx.reply(f"{user.mention} was timed out for 3 hours.\n(`Adjustable time coming soon.`)")
  """


def setup(client):
    client.add_cog(Moderation(client))

print("moderation.py fully loaded.")