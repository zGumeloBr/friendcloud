import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command()
    async def avatar(ctx, *, useravatar: discord.Member = None):
        if useravatar is None:
            user = ctx.author
        else:
            user = useravatar
        eavatar = discord.Embed(color=0x36393f, title=f'**<:quadro:716673073608130581> | Avatar de: {user.name}**')
        eavatar.set_image(url=user.avatar_url)
        await ctx.send(embed=eavatar)