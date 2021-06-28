import os
from decouple import config
import discord as dc
from discord import message

client = dc.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_messege(messege):
    print("[INFO] Messege recived")
    if messege.author == client.user:
        return

    msg = message.content

    if msg.startswith('!hello'):
        print("[INFO] recived a messege that start with !hello")
        await message.channel.send('Hello world!')


x = config('TOKEN')
client.run(x)
