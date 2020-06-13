import discord
import asyncio
import random
import time
import discloud
import datetime
from discord.ext import commands

def setup (client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command(name="kiss", usage="<<command>> <mensagem>")
    async def kiss(ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("<a:error:633826282114908160> **Digite alguem para beijar**.")
            return
        bj = ['https://i.imgur.com/i1PIph3.gif', 'https://i.imgur.com/WVSwvm6.gif', 'https://i.imgur.com/sZhtvBR.gif', 'https://i.imgur.com/So3TIVK.gif', 'https://i.imgur.com/q340AoA.gif', 'https://i.imgur.com/OjTBV8G.gif', 'https://i.imgur.com/SeCRpPp.gif', 'https://i.imgur.com/LRPJt19.gif']
        embed = discord.Embed(color=0x36393f, title = f'**<:beijo:716715561760981003> | Beijo**', description = f'<:beijo:716715561760981003> | {ctx.author.mention} você beijou deu um super beijo em {palavra}, espero que ele goste.')
        embed.set_image(url=f'{random.choice(bj)}')
        embed.set_thumbnail(url=client.user.avatar_url)
        await ctx.send(embed=embed)