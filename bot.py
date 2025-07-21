import discord
from discord.ext import commands
import os
import asyncio
import datetime
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")  # Usa variable de entorno por seguridad
INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print(f"[{datetime.datetime.now()}] ✅ BOT CONECTADO COMO {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Mantener el bot activo con reconexión automática
def iniciar_bot():
    keep_alive()
    while True:
        try:
            print("🟢 Iniciando bot...")
            bot.run(TOKEN)
        except Exception as e:
            print(f"🔴 Error: {e}")
            print("🔁 Reintentando en 5 segundos...")
            asyncio.sleep(5)

if __name__ == "__main__":
    iniciar_bot()
