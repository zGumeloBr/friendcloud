import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command(name="coffee", usage="<<command>> <mensagem>")
    async def coffe(ctx, *, pessoa=None):
        if pessoa is None:
            await ctx.send("<a:error:633826282114908160> **Digite alguem para entregar um delicioso café**.")
            return
        coffee = ['https://i.imgur.com/B68MhUu.gif']
        embed = discord.Embed(color=0x36393f, title = f'**<:cafe:716715535479603221> | Café**', description = f'<:cafe:716715535479603221> | {ctx.author.mention} deu uma xícara de café para {pessoa}, espero que ele goste.')
        embed.set_image(url=f'{random.choice(coffee)}')
        embed.set_thumbnail(url=client.user.avatar_url)
        await ctx.send(embed=embed)