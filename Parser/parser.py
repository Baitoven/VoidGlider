import discord
from discord.ext import commands
import os
import nacl

voice_client = discord.voice_client

async def parse(client, message):
    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/join'):
        await join_voice(message)

    if message.content.startswith('/leave'):
        await leave_voice(message)

    if message.content.startswith('/play'):
        await play_audio(client, message)

async def join_voice(message):
    channel = message.author.voice.channel
    voice_client = await channel.connect()

async def leave_voice(message):
    server = message.guild.voice_client
    await server.disconnect()

async def play_audio(client, message):
    if client.voice_clients == []:
        channel = message.author.voice.channel
        voice_client = await channel.connect()

    await voice_client.play(discord.FFmpegPCMAudio(executable=os.getenv('FFMPEG'), source="Audio/NeverGonnaGiveYouUp.mp3"))

    
