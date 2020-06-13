import discord
import asyncio
import random
import discloud
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command(name='kick', aliases=['expulsar'])
    @commands.bot_has_permissions(kick_members=True)
    async def _kick(ctx, member: discord.Member, *, reason: str = None):  # coloque self e use commands.command() se for cog
        if not ctx.author.guild_permissions.kick_members:
            return await ctx.send('**<:false:717395716502323230> | Você não tem permissão!**')
        try:
            motivo = reason if reason else "Nenhum motivo."
            await member.kick(reason=motivo)
            await ctx.send(f"**<:correct:717395741416488960> | O usuario {member} foi expulso com sucesso do servidor.  **")
        except discord.Forbidden:
            await ctx.send("**<:false:717395716502323230> | Não posso expulsar o usuário, o cargo dele está acima de mim.**")

    @_kick.error
    async def kick_error(ctx, error):  # coloque self se for cog
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("**<:false:717395716502323230> | Não tenho permissão de expulsar membros**")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("**<:false:717395716502323230> | O usuário não está no servidor.**")