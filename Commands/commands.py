import time
from discord.ext import commands
import discord
import os
from Audio.audioQueue import SongQueue, add_song_from_url
from Audio.youtube import load_from_url, parse_url

audioCachePath = 'Audio/AudioCache/'

def add_commands(bot):

    sgQueue = SongQueue()

    @bot.command(name='hello')
    async def Hello(context):
        await context.message.channel.send('Hello!')

    @bot.command(name='join')
    async def Join(context):
        if (context.author.voice): # If the person is in a channel
            channel = context.author.voice.channel
            await channel.connect()
        else: #But is (s)he isn't in a voice channel
            await context.send("You must be in a voice channel first so I can join it.")

    @bot.command(name='leave')
    async def Leave(context):
        if (context.voice_client): # If the bot is in a voice channel 
            await context.voice_client.disconnect() # Leave the channel
        else: # But if it isn't
            await context.send("I'm not in a voice channel, use the join command to make me join")

    @bot.command(name='play')
    async def Play(context):
        if (sgQueue.IsEmpty()):
            await context.send("Song queue is empty. Try queuing a new song with /queue first")
            return

        track = sgQueue.Take()

        if (context.voice_client):
            source = discord.FFmpegPCMAudio(source=audioCachePath + track["content"] + '.mp3', executable=os.getenv('FFMPEG'))
            voice = context.bot.voice_clients[0]
            voice.play(source=source, after=lambda error: PlayNext(context))
        else:
           await context.send("You must be in a voice channel first so I can join it.")

    def PlayNext(context):
        if (sgQueue.IsEmpty()):
            return

        track = sgQueue.Take()

        if (context.voice_client):
            source = discord.FFmpegPCMAudio(source=audioCachePath + track["content"] + '.mp3', executable=os.getenv('FFMPEG'))
            voice = context.bot.voice_clients[0]
            voice.play(source=source, after=lambda error: PlayNext(context))

    @bot.command(name='queue', pass_context=True)
    async def Queue(context, message):
        url = message.split(' ')[0]
        await add_song_from_url(sgQueue, url)
        await context.send("VoidGlider just finished queuing song " + url)

    @bot.command(name='skip')
    async def Next(context):
        if (sgQueue.IsEmpty()):
            await context.send("Song queue is empty. Try queuing a new song with /queue first")
            return
        PlayNext(context)
    
