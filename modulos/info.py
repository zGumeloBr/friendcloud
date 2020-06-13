import discord
import asyncio
import random
import time
import psutil
import discloud
import datetime
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command ()
    async def info(ctx):
           embed = discord.Embed(color=0x36393f, title='**<:interrogao:716672168641167401> | Info**:', description=f'Aqui estão algumas informações minhas:', timestamp=datetime.datetime.utcnow())
           embed.set_thumbnail(url=client.user.avatar_url)
           embed.add_field(name='**<:owner:633438913381269525> | Desenvolvedor:**', value='``zGumeloBr#8726``', inline=False)
           embed.add_field(name='**<:exclamao:716672212601405460> | Status:**', value=f'<:lista:716673135918972938>| ``Versão: 5.0 Ultimate``\n<:conexo:716672898433155182>| ``Ping: {round(client.latency * 1000)}ms``\n<:servidor:716673418266673174>| ``Servidores: {len(client.guilds)}``\n<:pessoas:716672313873137695>| ``Usuários: {len(client.users)}``', inline=False)
           embed.add_field(name='**<:ssd:716688118740418680> | Hospedagem:**', value=f'<:glitch:717390554819854386>| ``Host: Glitch``', inline=False)
           embed.add_field(name='**<:code:716691017939681361> | Código:**', value=f'<:python:716691326330208386>| ``Linguagem: Python``\n<:ram:716689762974564433>| ``Biblioteca: Discord.py``', inline=False)
           embed.add_field(name='**<:convite:633439670516187197> | Invite:**', value='[Clique Aqui!](https://discordapp.com/api/oauth2/authorize?client_id=633071376802250753&permissions=208037497&scope=bot)', inline=False)
           embed.add_field(name='**<:soma:633442206090264595> | Suporte:**', value='[Clique Aqui!](https://discord.gg/NsbV9Uk)', inline=False)
           await ctx.send(embed=embed)