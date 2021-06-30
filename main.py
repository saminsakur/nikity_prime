import discord
import random
import requests
import json
from words import *
from decouple import config


jokesUrl = r"https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"



def getJoke(u):
    r = requests.get(u)
    jo = json.loads(r.text)
    return jo

def matchwhole(content, list_to_match:list):
    return content in list_to_match

def matchstartswith(content, list_to_match:list):
    return any([content.startswith(i) for i in list_to_match])

class BotClient(discord.Client):
    async def on_ready(self):
        print(f"[Info] Logged in as {self.user.name} {self.user.id}")
        print("___________________________________________")


    async def on_message(self, message):
        if not message.author.id == self.user.id:
            print(f"[INFO] A messege have been recived from {message.author.name} {message.author.id}")

        if message.author.id == self.user.id:   
            print("[INFO] A messege has been sent")
            return                      # Make sure that the bot doesn't reply to itself

        msg = message.content

        if  matchwhole(msg, greetings_words):
            await message.reply(greetings_words[random.randint(0, len(greetings_words) -1)])

        elif matchstartswith(msg, health_question):
            await message.reply(health_question_response[random.randint(0, len(health_question_response) -1)])

        elif matchstartswith(msg, health_question_response):
            await message.reply(health_question_response_reply[random.randint(0 , len(health_question_response_reply) -1)])

        elif matchstartswith(msg, bot_question):
            await message.reply("Yes I am!")

        elif matchstartswith(msg, question_self_health):
            await message.reply("Oh! How are you? 😃")

        elif matchwhole(msg, ["Me too!", "me too!", "Me too", "me too"]):
            await message.reply("Ooo")

        elif msg == "ping":
            await message.reply("pong", mention_author=True)

        elif matchstartswith(msg, some_random_words):
            await message.reply("Hey! 😀", mention_author=True)

        elif matchstartswith(msg, ["Is Mahin a dumb?", "is mahin a dumb?"]):
            await message.reply("Yes he is 🤣")

        elif matchstartswith(msg, making_sad_words):
            await message.reply("Ouch! 🥺")

        elif matchstartswith(msg, x):
            await message.reply("Okay 🤐")
    
        elif matchstartswith(msg, thanking_words):
            await message.reply("Welcome!")

        elif message.content == "I'm from the east side of america":
            await message.reply(
                "Where we choose pride over character\nAnd we can pick sides, but this is us, this is us, this is")

        elif matchstartswith(msg, ["Who made you?", "who made you?", "Where are you from?"]):
            await message.channel.send("I'm a bot made by @sam.in#3588")

        elif matchstartswith(msg, ["!joke", "Tell a joke", "tell a joke", "Tell me a joke", "tell me a joke", "Joke please"]):
            jsonJoke = getJoke(jokesUrl)
            print(jsonJoke)
            jokeType = jsonJoke['type']
            setup = jsonJoke['setup']
            punchline = jsonJoke['punchline']
            await message.channel.send(f"**{jokeType}**\n{setup}\n{punchline}")

        # else:
        #    await message.reply("Sorry! cannot get that! 😶")


client = BotClient()
x = config('TOKEN')
client.run(str(x))
