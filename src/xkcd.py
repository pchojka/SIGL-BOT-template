import sys
from discord.ext import commands
import random
import requests
import json

@commands.command()
async def xkcd(ctx: commands.Context):
    data = requests.get('https://xkcd.com//info.0.json')
    last = data.json()
    lastest = int(last['num'])
    rand = random.randint(1, lastest)
    data2 = requests.get(f'https://xkcd.com/{rand}/info.0.json')
    ret = data2.json()
    await ctx.send(ret['img'])
    
sys.modules[__name__] = xkcd