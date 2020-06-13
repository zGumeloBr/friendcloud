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
    async def pet(ctx, *, palavra=None):
        bj = ['https://cdn.discordapp.com/attachments/716720178167283753/716720220877619280/8b53d5e386d2ebff3757989c63145ac3.gif']
        embed = discord.Embed(color=0x36393f, title = f'**<:heart:716719327948308531> | Pet**', description = f'<:heart:716719327948308531> | {ctx.author.mention} parabéns você adotou um jovem nuvem.')
        embed.set_image(url=f'{random.choice(bj)}')
        embed.set_thumbnail(url=client.user.avatar_url)
        await ctx.send(embed=embed)