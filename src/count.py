from discord.ext import commands
import discord
import sys




# Add all members of the servers into lists according to theirs status then display them in the channel wher the command was issued
@commands.command()
async def count(ctx: commands.Context):
    online = []
    offline = []
    dnd = []
    idle = []
    invisible = []
    for member in ctx.guild.members:
        if member.status == discord.Status.offline:
            offline.append(member)
        elif member.status == discord.Status.online:
            online.append(member)
        elif member.status == discord.Status.idle:
            idle.append(member)
        elif member.status == discord.Status.dnd or member.status == discord.Status.do_not_disturb:
            dnd.append(member)
        else:
            invisible.append(member)
    if len(online) > 0:
        await ctx.send("Members online")
        for i in online:
            await ctx.send(i)
    if len(offline) > 0:
        await ctx.send("Members offline")
        for i in offline:
            await ctx.send(i)
    if len(dnd) > 0:
        await ctx.send("Members do not disturb")
        for i in dnd:
            await ctx.send(i)
    if len(invisible) > 0:
        await ctx.send("Members invisible")
        for i in invisible:
            await ctx.send(i)
    if len(idle) > 0:
        await ctx.send("Members idle")
        for i in idle:
            await ctx.send(i)


sys.modules[__name__] = count