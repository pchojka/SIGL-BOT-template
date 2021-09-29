import os
from discord.ext import commands

DISCORD_TOKEN = os.getenv('DISCORD_KEY')

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 238762143485394944  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):  # When the bot is ready
    if message.content == "!name" :
        response = message.author
        await message.channel.send(response)

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = DISCORD_TOKEN
bot.run(token)  # Starts the bot