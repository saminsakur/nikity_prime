import os
import discord as dc
from discord import message

client = dc.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_messege(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!hello'):
        await message.channel.send('Hello! whatz going on!')


client.run(os.getenv("TOKEN"))