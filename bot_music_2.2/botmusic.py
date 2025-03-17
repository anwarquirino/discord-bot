import discord
from discord.ext import commands
import os
import yt_dlp as youtube_dl
from dotenv import load_dotenv
import asyncio
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Carregar variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Configuração do Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

# Tempo de inatividade (em segundos) para auto-desconectar
AUTO_DISCONNECT_TIMEOUT = 300  # 5 minutos

async def auto_disconnect(voice_client, text_channel, timeout=AUTO_DISCONNECT_TIMEOUT):
    """Auto-desconectar após período de inatividade."""
    await asyncio.sleep(timeout)
    if voice_client and not voice_client.is_playing():
        try:
            await voice_client.disconnect()
            await text_channel.send("Auto-desconectado por inatividade.")
            print("Auto-desconectado por inatividade.")
        except Exception as e:
            print("Erro ao desconectar:", e)

def get_youtube_url(query):
    """Buscar a melhor URL do YouTube com base em uma consulta"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        return info['entries'][0]['url'], info['entries'][0]['title']

def get_spotify_tracks(url):
    """Extrair títulos de músicas de um link do Spotify"""
    if "track" in url:
        track = sp.track(url)
        return [track["name"] + " " + track["artists"][0]["name"]]
    
    elif "playlist" in url:
        results = sp.playlist_tracks(url)
        return [track["track"]["name"] + " " + track["track"]["artists"][0]["name"] for track in results["items"]]
    
    elif "album" in url:
        results = sp.album_tracks(url)
        return [track["name"] + " " + track["artists"][0]["name"] for track in results["items"]]
    
    return None

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

@bot.command()
async def play(ctx, *, query: str):
    """Tocar música do YouTube ou Spotify"""
    if not ctx.author.voice:
        return await ctx.send("Você precisa estar em um canal de voz para tocar música!")

    channel = ctx.author.voice.channel
    if not ctx.voice_client:
        voice_client = await channel.connect()
    else:
        voice_client = ctx.voice_client

    # Se for um link do Spotify, buscar músicas
    if "spotify.com" in query:
        track_list = get_spotify_tracks(query)
        if not track_list:
            return await ctx.send("🚫 Não foi possível encontrar músicas no Spotify.")
        
        await ctx.send(f"🎵 Adicionando {len(track_list)} músicas da playlist/álbum...")
        for track in track_list:
            youtube_url, title = get_youtube_url(track)
            source = discord.FFmpegPCMAudio(youtube_url, options='-vn')
            voice_client.play(source)
            await ctx.send(f"🎵 Tocando agora: **{title}**")
    else:
        youtube_url, title = get_youtube_url(query)
        source = discord.FFmpegPCMAudio(youtube_url, options='-vn')
        voice_client.play(source)
        await ctx.send(f"🎵 Tocando agora: **{title}**")

    asyncio.create_task(auto_disconnect(voice_client, ctx.channel))

@bot.command()
async def pause(ctx):
    """Pausar a música"""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸️ Música pausada!")
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

@bot.command()
async def resume(ctx):
    """Retomar a música"""
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("▶️ Música retomada!")
    else:
        await ctx.send("Nenhuma música foi pausada.")

@bot.command()
async def stop(ctx):
    """Parar a música"""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹️ Música parada!")
        asyncio.create_task(auto_disconnect(ctx.voice_client, ctx.channel))
    else:
        await ctx.send("Nenhuma música está sendo reproduzida.")

@bot.command()
async def leave(ctx):
    """Desconectar o bot do canal de voz"""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("📤 Desconectado do canal de voz.")
    else:
        await ctx.send("Não estou em um canal de voz.")

# Iniciar o bot
bot.run(TOKEN)
