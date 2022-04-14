import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio
import random

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def play(self, ctx, url):
    if not ctx.author.voice:
      await ctx.reply("You're not connected to a voice channel. Please connect to one then run this command again.")
      return
    else:
      connecting = await ctx.reply("Connecting...")
      channel = ctx.author.voice.channel
      await channel.connect()
      await connecting.edit(content=f"Connected to {channel.mention}!")

    server = ctx.guild
    voice_channel = server.voice_client

    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=self.client.loop)
      voice_channel.play(player, after=lambda e: print(f"Player Error: %s" %e) if e else None)

    await ctx.send(f'**Now playing:** {player.title}')

  @commands.command(aliases=["leave"])
  async def disconnect(self, ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.message.add_reaction("👋")



def setup(client):
  client.add_cog(Music(client))

print("music.py fully loaded")