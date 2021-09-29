import os
from discord.ext import commands
from dotenv import load_dotenv
import discord
import count

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)

bot.add_command(count)

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')
    print('pong')



token = os.environ.get('TOKEN')
if not token :
    raise Exception('No Token')
bot.run(token)  # Starts the bot