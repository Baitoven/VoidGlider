from discord.ext import commands
import discord
import os
from Audio.youtube import load_from_url, parse_url

audioCachePath = 'Audio/AudioCache/'

def add_commands(bot):

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

    @bot.command(name='play', pass_context=True)
    async def Play(context, message):
        channel = context.author.voice.channel
        voice = await channel.connect()
    
        url = message.split(' ')[0]
        await load_from_url(url)
        track = audioCachePath + parse_url(url) + '.mp3'

        if (context.voice_client):
            source = discord.FFmpegPCMAudio(source=track, executable=os.getenv('FFMPEG'))
            voice.play(source, after=None)
        else:
           await context.send("You must be in a voice channel first so I can join it.") 
'''

async def play_audio(client, message):
    channel = message.author.voice.channel
    voice_client = await channel.connect()

    #url = message.content.split(' ')[1]
    #await load_from_url(url)
    #track = audioCachePath + parse_url(url) + '.mp3'

    #time.sleep(5)

    source = discord.FFmpegPCMAudio(source='oRSijEW_cDM.mp3', executable=os.getenv('FFMPEG'))
    time.sleep(1)
    voice_client.play(source, after=None) #try switching to external commands
'''
    
