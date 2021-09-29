import os
from discord.ext import commands
from dotenv import load_dotenv

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
async def pong(ctx):
    await ctx.send('pong')

<<<<<<< HEAD
token = "ODkyODIyMTE3Mjk1NDc2ODA2.YVSfZA.y5O1OtlVl0Bd3SKCR2D8V7EVb2E"
=======
token = os.environ.get('TOKEN')
if not token :
    raise Exception('No Token')
>>>>>>> 537aee5ae65c7fcdc4d304afd66cc373021c7778
bot.run(token)  # Starts the bot