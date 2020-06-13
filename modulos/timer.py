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
    async def timer(ctx):
        embed = discord.Embed(color=0x36393f, title = '**<:clock:716673390638923876> | Timer Iniciado**', description = f'Muito bem {ctx.author.mention} irei mandar um aviso em seu privado.')
        embed.add_field(name='**<:sino:716673450571464816> | Tempo:**', value='``5 minutos``', inline=False)
        await ctx.send(embed=embed)
        await asyncio.sleep(300)
        await ctx.author.send('<:sino:716673450571464816> **Prinn!!**')
        await ctx.author.send('<:sino:716673450571464816> **Prinn!!**')
        await ctx.author.send(f'**<:sino:716673450571464816> Prinnn!! {ctx.author.mention}, acorda dorminhoco seu despertador tocou.**') 