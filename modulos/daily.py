import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @client.command()
    async def daily(ctx):
        nuvens=['504', '1020', '2020', '34', '609', '10', '769', '49', '10469 🍀', '20']
        await ctx.send('> <:globo:716673039781330945> | Coletando nuvens...', delete_after=5)
        await asyncio.sleep(5)
        await ctx.send(f'> <:coin:716673011012337704> | **Parabéns, você coletou ``{random.choice(nuvens)} nuvens``, lembre-se você so pode coletar nuvens a cada ``24 horas``.**')