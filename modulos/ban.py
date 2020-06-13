import discord
import asyncio
import random
import discloud
from discord.ext import commands

def setup(client):

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command()
    async def ban(ctx, members: commands.Greedy[discord.Member], *, motivo: str = None):
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send('<:false:717395716502323230> | **Você não tem permissão para executar esse comando !**')
        try:
            if not motivo:
                motivo = ""
            for member in members:
                author = ctx.author.mention
                embed = discord.Embed(color=0x36393f,
                                  description=f'**<:correct:717395741416488960> | O usuario <@{member.id}> foi banido com sucesso**')
                embed.add_field(name='**<:pessoas:716672313873137695> | Autor:**', value=author)
                embed.add_field(name='**<:lista:716673135918972938> | Motivo:**', value=motivo)
                                      
            embed.set_footer(icon_url=ctx.guild.icon_url)
            embed.set_thumbnail(url=member.avatar_url)
            await member.ban(delete_message_days=1, reason=motivo)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        except IndexError:
            await ctx.send('**<:false:717395716502323230> | Você deve especificar um usuário para banir!**')
        except discord.Forbidden:
            await ctx.send(
            '**<:false:717395716502323230> | Não posso banir o usuário acima de mim ou não tenho permissão**!')
        finally:
            pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @client.command()
    async def unban(ctx, user_id=None):
        if user_id:
            try:
                user_id = int(user_id)
            except ValueError:
                return await ctx.send('**<:false:717395716502323230> | Isso não é um ID valido.**')
        else:
            return await ctx.send('**<:false:717395716502323230> | Digite o ID do usuário.**')
        try:
            user = await client.fetch_user(user_id)
        except discord.NotFound:
            await ctx.send('<:false:717395716502323230> | **Usuário não encontrado**')
        else:
            try:
                await ctx.guild.fetch_ban(user)
            except discord.NotFound:
                return await ctx.send('<:false:717395716502323230> | **O usuário não está banido**')
            texto = f"**<:correct:717395741416488960> | Membro ``{user.name}`` foi desbanido com sucesso.**"
            embed = discord.Embed(color=0x36393f, description=texto)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.guild.unban(user)
            await ctx.send(embed=embed)