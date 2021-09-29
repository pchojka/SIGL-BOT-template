import os
from discord.ext import commands
from dotenv import load_dotenv

import name

load_dotenv()

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx: commands.Context):
    await ctx.send('pong')

bot.add_command(name)

token = os.environ.get('TOKEN')
if not token :
    raise Exception('No Token')
bot.run(token)  # Starts the bot