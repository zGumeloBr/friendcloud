import discord
import asyncio
import random
import discloud
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command(name="say", usage="<<command>> <mensagem>")
    async def say(ctx, *, palavra=None):
        if not ctx.author.guild_permissions.manage_channels:
            return await ctx.send('**<:negado:633078061771915314> Você precisa da permissão ``Gerenciar Canais`` para enviar uma mensagem pelo bot!**')
        if palavra is None:
            await ctx.send("<a:error:633826282114908160> **Digite algo para eu anunciar**.")
            return
        embed = discord.Embed(color=0x36393f, description = f'{palavra}')
        await ctx.message.delete()
        await ctx.send(embed=embed)