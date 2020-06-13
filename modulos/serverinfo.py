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
    async def serverinfo(ctx):
           embed = discord.Embed(color=0x36393f, title='**<:discord:716677483008622632> | Server Info**:', description=f'**Informações do servidor: **``{ctx.guild.name}``', timestamp=datetime.datetime.utcnow())
           embed.set_thumbnail(url=ctx.guild.icon_url)
           embed.add_field(name='**<:coroa:716677801691971605> | Dono:**', value=ctx.guild.owner.name)
           embed.add_field(name='**<:pessoas:716672313873137695> | Membros:**', value=str(len(ctx.guild.members)), inline=False)
           embed.add_field(name='**<:etiqueta:716672975255896125> | Cargos:**', value=len(ctx.message.guild.roles), inline=False)
           embed.add_field(name='**<:lista:716673481013592086> | Emojis:**', value=len(ctx.guild.emojis), inline=False)
           embed.add_field(name='**<:rob:716678276579328003> | Bots:**', value=str(len([a for a in ctx.guild.members if a.bot])), inline=False)
           embed.add_field(name='**<:clock:716673390638923876> | Criado em:**', value=ctx.guild.created_at.strftime('%d %b %Y as %H:%M'), inline=False)
           embed.add_field(name='**<:globo:716673039781330945> | Região:**', value=str(ctx.guild.region).title(), inline=False)
           await ctx.send(embed=embed)