import discord
import asyncio
import random
import secrets
import time
import discloud
import datetime
from datetime import datetime
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command()
    async def fofura(ctx):
        fofura = ['https://i.imgur.com/otUToTY.gif', 'https://i.imgur.com/hhyDZA8.gif']
        embed = discord.Embed(color=0x36393f, title = f'**<:fofo:716718025839083580> | Fofura**', description = f'<:fofo:716718025839083580> | {ctx.author.mention} aproveite esse momento fofura.')
        embed.set_image(url=f'{random.choice(fofura)}')
        embed.set_thumbnail(url=client.user.avatar_url)
        await ctx.send(embed=embed)