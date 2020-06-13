import discord
import asyncio
import random
import secrets
import time
import discloud
import datetime
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = 'c!')

for extension in __import__("pathlib").Path('./modulos').glob('**/*.py'):
    ext_file = str(extension).replace('/','.').replace('\\','.')[:-3]
    ext_name = '.'.join(ext_file.split('.')[1:])
    try:
        client.load_extension(ext_file)
        print(f"✔️ - Módulo [{ext_name}] carregado!")
    except commands.NoEntryPointError:
        if not str(extension).startswith("_"):
            print(f'⚠ - Módulo [{ext_name}] ignorado! "def setup" não encontrado!!')
    except:
        print(f"\n\n{'='*10} [{ext_name}] Falhou! {'='*70}\n\n{__import__('traceback').format_exc()}\n{'-' * 100}")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('☁ | Prefix c!.'))
    print('▂▂▂  Status ▂▂▂')
    print(f'☁ - Programa [Friend Cloud.py] iniciado!')
    print(f'☁ - Status de rede em [{round(client.latency * 1000)}ms]')
    print('▂▂▂  Logs ▂▂▂')
    if not hasattr(client, 'uptime'):
        client.uptime = datetime.utcnow()
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x36393f, description = f'<a:error:633826282114908160> **{ctx.author.mention} este comando não está registrado no meu banco de dados, consulte meus comandos usando o comando ``c!help``**')
        await ctx.send(embed=embed, delete_after=3)
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(color=0x36393f, description = f'<a:error:633826282114908160> **{ctx.author.mention} Espere um pouco para usar o comando novamente**')
        await ctx.send(embed=embed, delete_after=3)

@client.event
async def on_member_join(member):
    if member.guild.id != 716640582243450900: 
        return
    else:
        canal = client.get_channel(716640582281461796)
        role = member.guild.get_role(716640582243450903) 
        embed = discord.Embed(color=0x36393f, description = f'**<:sino:716673450571464816> | Temos um novo membro.**')
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name='**<:porta:716704742104891433> | Seja Bem-Vindo**', value=f'Olá {member.mention} seja bem-vindo à **Cloud Party**, uma incrivel comunidade onde você sempre pode fazer novos amigos.', inline=False)
        embed.add_field(name='**<:prefix:716674101183512626> | Prefixo:**', value=f'``c!``', inline=True)
        embed.add_field(name='**<:discord:716677483008622632> | Invite:**', value=f'[Clique Aqui!](https://discordapp.com/api/oauth2/authorize?client_id=633071376802250753&permissions=2147483127&scope=bot)', inline=False)
        await canal.send(embed=embed)
        await member.add_roles(role)


client.run('Ai ja e um segredinho')
