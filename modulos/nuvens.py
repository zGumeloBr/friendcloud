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
    async def nuvens(ctx):
        banco=['Como vamos armazenar algo assim? Nuvens não tem peso.', 'Pois bem seu saldo atual e de ``0``, pois todo seu dinheiro foi destinado a pagar suas dividas.', 'Nosso banco foi roubado por uma nuvem furiosa, sentimos muito.', 'Explendido! Nossos cientistas descobriram um metodo de armazenar nuvens, mas você foi roubado antes desse dia.', 'Seu cartão foi clonado e seu dinheiro roubado, sentimos muito.']
        await ctx.send(f'> **<:coin:716673011012337704> | {random.choice(banco)}**')