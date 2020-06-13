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
    async def gerarsenha(ctx, nbytes: int = 18):
        if nbytes not in range(3, 1401):
            return await ctx.send("<:drive:716696097460060172> | Eu aceito apenas números entre ``3-1400``")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"<:carta:716672345963757689> | Enviando uma mensagem particular para você com sua senha gerada aleatoriamente **{ctx.author.name}**")
            await ctx.author.send(f"<:presente:716673358439252038> | **Aqui está sua senha:**\n``{secrets.token_urlsafe(nbytes)}``")