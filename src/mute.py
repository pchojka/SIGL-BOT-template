import sys
import discord
from discord.ext import commands
from discord.permissions import Permissions
from discord.utils import get

@commands.command()
async def mute(ctx: commands.Context, user: discord.Member = None):

    # If no user is specified
    if not (user and isinstance(user, discord.Member)):
        await ctx.send("Usage: !mute <user>")
        return

    # Get the Ghost role
    ghostRole = get(ctx.guild.roles, name="Ghost")

    # If the Ghost role doesn't exist, create it
    if not ghostRole :
        ghostRole = await ctx.guild.create_role(
            name="Ghost",
            colour=discord.Colour(0xD8D8D8),
            permissions=Permissions(103080329792)
        )

    # Toggle the role
    if not ghostRole in user.roles :
        await user.add_roles(ghostRole)
        await ctx.send(user.display_name + " is now muted!")
    else :
        await user.remove_roles(ghostRole)
        await ctx.send(user.display_name + " is now unmuted!")

sys.modules[__name__] = mute
