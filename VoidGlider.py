from Commands.commands import add_commands
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

add_commands(bot)

#bot.add_command(Coucou)
bot.run(os.getenv('DISCORD_TOKEN'))

