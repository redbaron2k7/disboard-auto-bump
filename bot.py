import discord
import datetime
from dotenv import load_dotenv
import os
import asyncio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')
CHANNEL_IDS = os.getenv('CHANNEL_IDS').split(',')

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

    while True:
        for channel_id in CHANNEL_IDS:
            channel = client.get_channel(int(channel_id.strip()))

            if channel is not None:
                guild_id = channel.guild.id
                async for message in channel.history():
                    if message.author.id == 302050872383242240:  # This is the ID of Disboard
                        embed = message.embeds[0]
                        if 'Bump done' in embed.description:
                            print("Bump detected. Guild: " + str(guild_id) + " Channel: " + str(channel))
                            msg_time = message.created_at
                            if (datetime.datetime.now(datetime.timezone.utc) - msg_time).total_seconds() > 7200:
                                await bump(client, guild_id, channel)
                                await channel.send('Bumped the server! Check my bio!')
                        break

        await asyncio.sleep(60)

async def bump(client, guild_id, channel):
    guild = channel.guild
    command_name = 'bump'
    command = None
    async for cmd in channel.slash_commands():
        if cmd.name == command_name:
            command = cmd
            break
    if command:
        await command(channel=channel)
    else:
        print(f"Slash command '{command_name}' not found.")

client.run(TOKEN)