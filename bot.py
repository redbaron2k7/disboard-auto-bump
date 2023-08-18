import discord
from discord.ext import commands
import datetime
from dotenv import load_dotenv
import os
from flask import Flask
from threading import Thread
import requests
import json

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
                        send_bump_request(channel.id, guild_id)
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
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json',
    }

    payload = {
        "type": 2,
        "application_id": "302050872383242240",
        "guild_id": str(guild_id),
        "channel_id": str(channel_id),
        "session_id": "d61f0ce1f0b8fd4570ae2a489fa75cd9",
        "data": {
            "version": "1051151064008769576",
            "id": "947088344167366698",
            "name": "bump",
            "type": 1,
            "options": [],
            "application_command": {
                "id": "947088344167366698",
                "application_id": "302050872383242240",
                "version": "1051151064008769576",
                "default_member_permissions": None,
                "type": 1,
                "nsfw": False,
                "name": "bump",
                "description": "Pushes your server to the top of all your server's tags and the front page",
                "description_localized": "Bump this server.",
                "dm_permission": True,
                "contexts": None
            },
            "attachments": []
        },
        "nonce": "1141916587096276992"
    }

    response = requests.post('https://canary.discord.com/api/v9/interactions', headers=headers, data=json.dumps(payload))

    print(response.status_code)

keep_alive()
bot.run(TOKEN)