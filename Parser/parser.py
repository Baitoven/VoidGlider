import discord
import os
from Audio.youtube import *
import time

voice_client = discord.voice_client
audioCachePath = 'Audio/AudioCache'

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

    #url = message.content.split(' ')[1]
    #await load_from_url(url)
    #track = audioCachePath + parse_url(url) + '.mp3'

    #time.sleep(5)

    source = discord.FFmpegPCMAudio('oRSijEW_cDM.mp3')#, executable=os.getenv('FFMPEG'))
    voice_client.play(source)

    
