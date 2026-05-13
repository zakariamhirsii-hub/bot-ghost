import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Not strictly needed on Render if you set env vars directly

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(
        name='streaming-name', 
        url='https://www.twitch.tv/urtwitchusername'
    ))

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN environment variable not set")

bot.run(TOKEN)
