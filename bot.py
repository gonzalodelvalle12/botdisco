import discord
from discord.ext import commands
import os
import datetime
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"[{datetime.datetime.now()}] ✅ Bot activo como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

def iniciar_bot():
    keep_alive()
    while True:
        try:
            print("🟢 Iniciando bot...")
            bot.run(TOKEN)
        except Exception as e:
            print(f"🔴 Error: {e}, reintentando...")

if __name__ == "__main__":
    iniciar_bot()

