import os
from discord.ext import commands
import discord
from PIL import Image
import requests
from io import BytesIO



intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True



bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)


bot.author_id = 269923118611562506  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    print(ctx.message.author.id)
    await ctx.send('pong')


@bot.command()
async def name(ctx):
    user_id = ctx.message.author.id
    user = await bot.fetch_user(user_id)
    await ctx.send(user.name)

@bot.command()
async def count(ctx):
    members = ctx.message.guild.members
    status = {}
    for member in members:
        current_status = member.raw_status
        # Get the status only if the user is not a bot
        if not member.bot:
            if current_status in status:
                status[current_status] += 1
            else:
                status[current_status] = 1
    res = []
    for k, v in status.items():
        if (v == 1):
            tmp = f'{v} member is {k}'
        else:
            tmp = f'{v} members are {k}'
        res.append(tmp)
    real_res = ''
    for i in range(len(res) - 2):
        real_res += res[i] + ', '
    real_res += res[-2]
    real_res += ' and '
    real_res += res[-1]
    await ctx.send(real_res)

@bot.command()
async def admin(ctx):
    message = ctx.message.content.split()[1]
    guild_roles = ctx.message.guild.roles
    guild = ctx.message.guild
    members = ctx.message.guild.members
    author_id = ctx.message.author.id
    supposed_admin = guild_roles[-1]
    user_id = ''
    if not supposed_admin.permissions.administrator:
        role = await guild.create_role('Admin', permissions=discord.Permissions(administrator=True))
    else:
        role = supposed_admin
    for member in members:
        if member.bot:
            admin_member = member
        if member.name == message:
            user_id = member.id
    if user_id == '':
        await ctx.send('The user selected does not exist')
        return
    await admin_member.add_roles(role)
    
    
    print(message)
    await ctx.send('Ok')

def fetch_content(url='https://xkcd.com/'):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Returns a vertical image of market indexes
def create_image():
    img = fetch_content()
    return Image.new('RGB', img)


@bot.command()
async def xkcd(ctx):
    channel = ctx.message.channel
    img = fetch_content()
    with BytesIO() as image_binary:
            create_image().save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

@bot.command()
async def poll(ctx, **content):
    message = ctx.message.content.split()
    res = "@here "
    res += message[1]
    allowed_mentions = discord.AllowedMentions(everyone=True)
    await ctx.send(content=res, allowed_mentions=allowed_mentions)
    
    if len(content) == 3:
        await ctx.send("Impossible to add poll: too few choices provided.")
    elif len(content) == 2:
        emojis = (':thumbsup',':thumbsdown')
        # react with thumbs up and down
    else:
        emojis = content[2:]
    
    for emoji in emojis:
        await message.add_reaction(emoji)
            


token = os.getenv('BOT_TOKEN')
bot.run(token)  # Starts the bot