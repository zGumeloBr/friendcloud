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
    async def cassino(ctx):
        emojis = ['<:melao:716673263782330388>', '<:pera:716673323487985666>', '<:morango:716673292572033065>', '<:melancia:716673219498606622>', '<:maca:716673185134936076>', '<:limo:716672270868807741>', '<:cereja:716672242792267806>']
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**| {a} {b} {c} |\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} ``Todos combinando, você ganhou!`` <:premio:716698574116618240>")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} ``2 em uma fileira, você ganhou!`` <:premio:716698574116618240>")
        else:
            await ctx.send(f"{slotmachine} ``Sem correspondência, você perdeu`` <:triste:716699427347103784>")