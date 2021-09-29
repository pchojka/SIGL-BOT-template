import sys
import discord
from discord.ext import commands
from discord.permissions import Permissions
from discord.utils import get

@commands.command()
async def admin(ctx: commands.Context, user: discord.Member = None):

    # If no user is specified
    if not (user and isinstance(user, discord.Member)):
        await ctx.send("Usage: !admin <user>")
        return

    # Get the Admin role
    adminRole = get(ctx.guild.roles, name="Admin")

    # If the Admin role doesn't exist, create it
    if not adminRole :
        adminRole = await ctx.guild.create_role(
            name="Admin",
            colour=discord.Colour(0x0062ff),
            permissions=Permissions(8)
        )

    # Add the role to the selected user
    await user.add_roles(adminRole)

    await ctx.send(user.display_name + " is now administrator!")


sys.modules[__name__] = admin
