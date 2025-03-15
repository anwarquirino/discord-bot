import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import wavelink

# Carregar variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento quando o bot está pronto
@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")
    # Conectar o bot ao Lavalink quando ele estiver pronto
    await bot.load_extension("music")

# Comandos do bot
@bot.command()
async def ping(ctx):
    """Comando básico para testar o bot"""
    await ctx.send(f"Pong! 🏓 ({round(bot.latency * 1000)}ms)")

# Inicializando a conexão com Lavalink
@bot.event
async def on_ready():
    print(f"{bot.user} conectado ao Discord!")
    
    # Conectando ao Lavalink
    await bot.wait_until_ready()
    node = await wavelink.NodePool.create_node(
        bot=bot,
        host='localhost',  # Ou o IP do servidor Lavalink
        port=2333,  # A porta padrão do Lavalink
        password='youshallnotpass'  # A senha que você configurou no Lavalink
    )
    print(f"Conectado ao Lavalink: {node}")

# Comando para tocar música
@bot.command()
async def play(ctx, *, query: str):
    """Tocar música"""
    # Verificar se o usuário está em um canal de voz
    if not ctx.author.voice:
        return await ctx.send("Você precisa estar em um canal de voz para tocar música!")
    
    channel = ctx.author.voice.channel

    # Conectar ao canal de voz
    voice_client = await channel.connect()

    # Buscar a música com o Wavelink
    track = await wavelink.YouTubeTrack.search(query)

    # Reproduzir a música
    await voice_client.play(track[0])

    await ctx.send(f"Tocando: {track[0].title}")

# Comando para pausar a música
@bot.command()
async def pause(ctx):
    """Pausar a música"""
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Música pausada!")
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

# Comando para parar a música
@bot.command()
async def stop(ctx):
    """Parar a música"""
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Música parada!")
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

# Comando para desconectar do canal de voz
@bot.command()
async def disconnect(ctx):
    """Desconectar o bot do canal de voz"""
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Desconectado do canal de voz.")
    else:
        await ctx.send("Não estou em um canal de voz.")

# Iniciar o bot
bot.run(TOKEN)
