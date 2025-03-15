import discord
from discord.ext import commands
import os
import yt_dlp as youtube_dl
from dotenv import load_dotenv

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

# Comando para tocar música sem Lavalink
@bot.command()
async def play(ctx, *, query: str):
    """Tocar música do YouTube"""
    # Verificar se o usuário está em um canal de voz
    if not ctx.author.voice:
        return await ctx.send("Você precisa estar em um canal de voz para tocar música!")
    
    channel = ctx.author.voice.channel

    # Conectar ao canal de voz
    if not ctx.voice_client:
        voice_client = await channel.connect()
    else:
        voice_client = ctx.voice_client

    # Configuração do youtube_dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extractaudio': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        url = info['entries'][0]['url']
        title = info['entries'][0]['title']

    # Criar um FFmpeg player
    ffmpeg_opts = {
        'options': '-vn',
    }

    source = discord.FFmpegPCMAudio(url, **ffmpeg_opts)
    voice_client.play(source)

    await ctx.send(f"🎵 Tocando agora: **{title}**")

# Comando para pausar a música
@bot.command()
async def pause(ctx):
    """Pausar a música"""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸️ Música pausada!")
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

# Comando para retomar a música
@bot.command()
async def resume(ctx):
    """Retomar a música"""
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("▶️ Música retomada!")
    else:
        await ctx.send("Nenhuma música foi pausada.")

# Comando para parar a música
@bot.command()
async def stop(ctx):
    """Parar a música"""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹️ Música parada!")
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

# Comando para desconectar do canal de voz
@bot.command()
async def disconnect(ctx):
    """Desconectar o bot do canal de voz"""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("📤 Desconectado do canal de voz.")
    else:
        await ctx.send("Não estou em um canal de voz.")

# Iniciar o bot
bot.run(TOKEN)
