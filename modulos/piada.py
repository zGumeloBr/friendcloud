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
    async def piada(ctx):
        tipo =['O garoto apanhou da vizinha, e a mãe furiosa foi tomar satisfação: Por que a senhora bateu no meu filho? Ele foi mal-educado, e me chamou de gorda. E a senhora acha que vai emagrecer batendo nele?', 'Doutor, como eu faço para emagrecer? Basta a senhora mover a cabeça da esquerda para a direita e da direita para a esquerda. Quantas vezes, doutor? Todas as vezes que lhe oferecerem comida.', 'A mulher comenta com o marido: Querido, hoje o relógio caiu da parede da sala e por pouco não bateu na cabeça da mamãe... Maldito relógio. Sempre atrasado...', 'O condenado à morte esperava a hora da execução, quando chegou o padre: Meu filho, vim trazer a palavra de Deus para você. Perda de tempo, seu padre. Daqui a pouco vou falar com Ele, pessoalmente. Algum recado?', 'Um advogado e sua sogra estão em um edifício em chamas. Você só tem tempo pra salvar um dos dois. O que você faz? Você vai almoçar ou vai ao cinema?', 'Mamãe, mamãe... na escola me chamaram de mentiroso. Cale-se que você nem vai à escola ainda...', 'O que fala o livro de Matemática para o livro de História? R: Não me venha com história que eu já estou cheio de problema!', 'Do que diabo morreu? De diabetes', 'O que é preciso para reunir os Beatles? Mais duas balas', 'Um oficial iraquiano chama os oito sósias do Saddam e diz: Tenho boas e más notícias. A boa notícia é que Saddam está vivo. Todos os sósias comemoram. A má notícia é que ele perdeu um braço.', 'Um homem chega na balada e encontra uma mulher e então dá um garfo a ela. E ela pergunta: para quê o garfo, e ele responde: é por que eu to dando sopa, e ela diz: mas sopa se come de colher, e ele responde: é que eu sou difícil...', 'Como é que se faz um monte de velhinhas gritar "Mer*da"? É só gritar "Bingo"', 'No balcão da Alfandega: Seu nome ? Abu Abdalah Sarafi. Sexo? Quatro vezes por semana. Não, não, não! Homem ou mulher? Homem, mulher. Algumas vezes camelo.', 'Qual a diferença entre um político e um cachorro atropelados? antes do cachorro, há marcas de freada...', 'Um eletricista vai até a UTI de um hospital, olha para os pacientes ligados a diversos tipos de aparelhos e diz-lhes: Respirem fundo: vou trocar o fusível.']
        embed = discord.Embed(color=0x36393f,  description = f'**<:maca:716673185134936076> | Olha a piada:** {random.choice(tipo)}')
        await ctx.send(embed=embed)