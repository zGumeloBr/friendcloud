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
    async def invite(ctx):
        embed = discord.Embed(color=0x36393f, description = f'**<:globo:716673039781330945> | Meu link de invite.**')
        embed.add_field(name='**<:convite:633439670516187197> | Link:**', value='[Clique Aqui!](https://discordapp.com/api/oauth2/authorize?client_id=633071376802250753&permissions=208037497&scope=bot)', inline=False)
        await ctx.send(embed=embed)