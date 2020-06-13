import discord
import asyncio
import random
import discloud
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command()
    async def clear(ctx, quantidade: int):
        if not ctx.author.guild_permissions.manage_messages:
            return await ctx.send('**<:false:717395716502323230> | Você não possui permissão a permissão ``Gerenciar Mensagens`` para limpar o chat!**')
        if ctx.author.guild_permissions.manage_messages:
            try:
                await ctx.message.delete()
                await ctx.channel.purge(limit=quantidade)
                embed = discord.Embed(color=0x36393f, description=f'<:correct:717395741416488960> | ``{quantidade}`` **mensagens apagadas com Sucesso!** ')
                await ctx.send(embed=embed)
            finally:
                pass