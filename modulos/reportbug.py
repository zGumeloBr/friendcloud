import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @client.command(name="reportbug", usage="<<command>> <mensagem>")
    async def reportbug(ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("<a:error:633826282114908160> **Informe o bug, por gentileza.**.")
            return
        canal = client.get_channel(716640583216660554)
        embed = discord.Embed(color=0x36393f, title='**<:bug:716673104000057414>  Bug Reportado.**')
        embed.add_field(name = '**<:pessoas:716672313873137695> | Autor**', value=f'{ctx.author.mention}', inline=False)
        embed.add_field(name = '**<:bug:716673104000057414>  | Bug**', value=f'{palavra}', inline=False)
        await ctx.send('> <:suporte:716697513700360413> | **Obrigado por reportar esse bug, mas lembre-se esse comando de delay de ``24h``**')
        await canal.send(embed=embed)