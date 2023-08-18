import discord
from discord.ext import commands
import datetime
from dotenv import load_dotenv
import os
from flask import Flask
from threading import Thread

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = commands.Bot(command_prefix=PREFIX)

@bot.listen()
async def on_ready():
    print('Bot is ready.')

    channel = bot.get_channel(int(CHANNEL_ID))

    if channel is not None:
        guild_id = channel.guild.id
        async for message in channel.history():
            if message.author.id == 302050872383242240: # This is the ID of Disboard
                embed = message.embeds[0]
                if 'Bump done' in embed.description:
                    print("Bump detected")
                    msg_time = message.created_at
                    if (datetime.datetime.now(datetime.timezone.utc) - msg_time).total_seconds() > 7200:
                        await channel.send('Bumping Server...')
                        await send_bump_request(channel.id, guild_id)
                break

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def send_bump_request(channel_id, guild_id):
    guild = bot.get_guild(guild_id)
    command = await guild.fetch_command('bump')
    await command.invoke()

keep_alive()
bot.run(TOKEN)