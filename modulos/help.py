import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    client.remove_command("help") 
    @client.command (aliases=["ajuda"])
    async def help(ctx):
        embed = discord.Embed(color=0x36393f, title='**<:interrogao:716672168641167401> | Ajuda**:', description=f'Olá meu nome é ``Friend Cloud`` e um prazer em conhece-lo, Bem eu sou um simples Bot para a ``Moderação, Diversão e Informações`` do seu servidor espero que goste das minhas funções.', timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name='**<:prefix:716674101183512626> | Prefixo:**', value='``c!``', inline=False)
        embed.add_field(name='**<:cmd:716654612911882302> | Moderação:**', value='``clear, ban, unban, kick, say``', inline=False)
        embed.add_field(name='**<:gear:716672377957777449> | Utilitarios:**', value='``info, serverinfo, cmdhelp, ping, timer, invite``', inline=False)
        embed.add_field(name='**<:ballon:716655069973446726> | Diversão:**', value='``avatar, piada, pet, coffee, kiss, fofura, cassino, gerarsenha.``', inline=False)
        embed.add_field(name='**<:coin:716673011012337704> | Economia:**', value='``daily, nuvens``', inline=False)
        embed.add_field(name='**<:bug:716673104000057414> | Central:**', value='``reportbug`` (Use esse comando para reportar um bug para a nosso central, formato: c!bug [Bug])', inline=False)
        await ctx.send(embed=embed)