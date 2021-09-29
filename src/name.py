import sys
from discord.ext import commands

@commands.command()
async def name(ctx: commands.Context):
    await ctx.send(ctx.author)

sys.modules[__name__] = name