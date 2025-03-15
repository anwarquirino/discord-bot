import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

@bot.command()
async def ping(ctx):
    """Comando básico para testar o bot"""
    await ctx.send(f"Pong! 🏓 ({round(bot.latency * 1000)}ms)")

# Iniciar o bot
bot.run(TOKEN)
