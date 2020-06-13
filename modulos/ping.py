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
    async def ping(ctx):
        embed = discord.Embed(color=0x36393f, description = f'**<:conexo:716672898433155182> | Estou rodando a ``{round(client.latency * 1000)}ms``**')
        await ctx.send(embed=embed)