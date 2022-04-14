import discord
from discord.ext import commands
from discord_components import *

DiscordComponents(client)

class Socials(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["slendsocials", "website", "slendwebsite"])
  async def socials(self, ctx):
    embed = discord.Embed(title="A Blended Website", description="Hey, thanks for wanting to   check out Slend's social medias! He has made a website where they're all kept, so the button below will take you to it.", color=0xff8800)
    embed.set_footer(text="Please note that this website is still in development and may not look/function the best.")
  
    await ctx.reply(
      embed=embed,
      components=[
        Button(style=ButtonStyle.URL, label="Go to A Blended Website", url="https://a-blended-website.gq/")
      ],
    )
  
  
  
  @commands.command()
  async def youtube(self, ctx):
    embed = discord.Embed(title="Slend's YouTube can be found here:", description="Hey, thanks for   wanting to check out Slend's YouTube. I have a few accounts, so here's a few buttons so you can   choose exactly which channel you want to go to:",   color=0xFF0000)
  
    await ctx.reply(
      embed=embed,
      components=[
        Button(style=ButtonStyle.URL, label="A Blended Website", url="https://a-blended-website.gq"),
        Button(style=ButtonStyle.URL, label="YouTube -   Slender the Blender",   url="https://www.youtube.com/channel/UC1Lb5yNlj9pgy0TyzuSjTA"),
        Button(style=ButtonStyle.URL, label="YouTube -   Slender the Other Blender",   url="https://www.youtube.com/channel/UCkGWfABIcdqOqiNn9gx-IIA"),
        Button(style=ButtonStyle.URL, label="YouTube -   Slend_K Clips and VoDs",   url="https://www.youtube.com/channel/UCsCCoYnmqeKcfsOoY8DgbNg"),
      ],
    )
  
  @commands.command()
  async def Twitch(self, ctx):
    embed = discord.Embed(title="Slend's Twitch can be   found here:", description="Here's a button to be taken right to the Twitch Channel!", color=0x9147ff)
  
    await ctx.reply(
      embed=embed,
      components=[
        Button(style=ButtonStyle.URL, label="A Blended Website", url="https://a-blended-website.gq"),
        Button(style=ButtonStyle.URL, label="Twitch - Slend_K", url="https://www.twitch.tv/slend_k"),
      ],
    )
  
  @commands.command()
  async def Twitter(self, ctx):
    embed = discord.Embed(title="Slend's Twitter can be found here:", description="Hey, thanks for   wanting to check out Slend's Twitter.",   color=0x1d9bf0)
  
    await ctx.reply(
      embed=embed,
      components=[
        Button(style=ButtonStyle.URL, label="A Blended Website",   url="https://a-blended-website.gq"),
        Button(style=ButtonStyle.URL, label="Twitter -   @SlendBlender",   url="https://www.twitter.com/SlendBlender")
      ],
    )



  



def setup(client):
    client.add_cog(Socials(client))

print("socials.py fully loaded.")