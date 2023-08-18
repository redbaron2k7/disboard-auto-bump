import discord
from discord.ext import commands
import datetime
from dotenv import load_dotenv
import os
import threading
from flask import Flask
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')
CHANNEL_IDS = os.getenv('CHANNEL_IDS').split(',')

bot = commands.Bot(command_prefix=PREFIX)

@bot.listen()
async def on_ready():
    print('Bot is ready.')

    while True:
        threads = []
        for channel_id in CHANNEL_IDS:
            channel = bot.get_channel(int(channel_id.strip()))

            if channel is not None:
                guild_id = channel.guild.id
                thread = threading.Thread(target=check_bump_availability, args=(channel.id, guild_id))
                thread.start()
                threads.append(thread)

        for thread in threads:
            thread.join()

        time.sleep(5)

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

async def send_bump_request(channel_id, guild_id):
    guild = bot.get_guild(guild_id)
    command = await guild.fetch_command('bump')
    await command.invoke()

def check_bump_availability(channel_id, guild_id):
    channel = bot.get_channel(channel_id)
    if channel is not None:
        async def check_single_channel():
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
        asyncio.run(check_single_channel())

keep_alive()
bot.run(TOKEN)