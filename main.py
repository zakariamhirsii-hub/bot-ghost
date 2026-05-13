import discord
import os
import threading
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

# --- Create a simple web server for keep-alive ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return "OK", 200

def run_web_server():
    # Render assigns the PORT environment variable automatically
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- Discord Bot Code ---
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    await bot.change_presence(
        activity=discord.Streaming(
            name='ᑌTOPIΛ network',
            url='https://discord.gg/RRCjw6XWy'
        )
    )
    print('🎮 Status updated')

# Start the web server in a separate thread
threading.Thread(target=run_web_server, daemon=True).start()

# Run the bot
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN environment variable not set")
    
bot.run(TOKEN)
