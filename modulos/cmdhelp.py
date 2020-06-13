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
    async def cmdhelp(ctx):
           embed = discord.Embed(color=0x36393f, title='**<:interrogao:716672168641167401> Comandos**:', description=f'Aqui estÃ£o algumas informaÃ§Ãµes sobre os meus comandos:', timestamp=datetime.datetime.utcnow())
           embed.set_thumbnail(url=client.user.avatar_url)
           embed.add_field(name='**<:interrogao:716672168641167401> | Clear:**', value='Comando para ``limpar`` o chat do servidor, exemplo: ``c!clear 999``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Ban:**', value='Comando para ``banir`` um usuÃ¡rio do servidor, exemplo: ``c!ban (user) (motivo)``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Unban:**', value='Comando para ``desbanir`` um usuÃ¡rio do servidor, exemplo: ``c!unban (user)``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Kick:**', value='Comando para ``exepulsar`` um usuÃ¡rio do servidor, exemplo: ``c!kick (user)``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Info:**', value='Comando para ver as ``informaÃ§Ãµes`` do bot, exemplo: ``c!info``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Serverinfo:**', value='Comando para ver as informaÃ§Ãµes do servidor, exemplo: ``c!serverinfo``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Avatar:**', value='Comando para ver o seu avatar em maior resoluÃ§Ã£o, exemplo: ``c!avatar``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Piada:**', value='Comando para o bot contar uma piada: ``c!piada``', inline=False) 
           embed.add_field(name='**<:interrogao:716672168641167401> | Timer:**', value='Comando para criar um simples timer: ``c!timer``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Say:**', value='Comando para ``mandar`` uma mensagem atraves do bot, exemplo: ``c!say OlÃ¡``', inline=False)
           embed.add_field(name='**<:interrogao:716672168641167401> | Anuncio:**', value='Comando para ``enviar`` um anuncio atraves do bot, exemplo: ``c!anuncio O mundo ira acabar)``', inline=False)
           await ctx.send('> <:interrogao:716672168641167401>**Enviando em seu privado...**')              
           await ctx.author.send(embed=embed)