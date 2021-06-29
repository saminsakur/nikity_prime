import discord
from decouple import config

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"[Info] Logged in as {self.user.name} {self.user.id}")
        print("####################")
    async def on_message(self, message):
        # if message.author.id == self.user.id:
        #     return

        if message.content.startswith('hello'):
            await message.channel.send('Hello! how are you?')

client = MyClient()
x = config('TOKEN')
client.run(str(x))
