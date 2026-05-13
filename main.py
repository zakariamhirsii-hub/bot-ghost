import discord
import os
from discord.ext import commands

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='streaming-name', url='https://www.twitch.tv/urtwitchusername'))

# Get token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not TOKEN:
    raise ValueError("No token found. Please set DISCORD_BOT_TOKEN in your .env file or environment variables")

bot.run(TOKEN)