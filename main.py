"""
    ----------------
    | NIKITY PRIME |
    ----------------
    A discord bot

    Author - Samin Sakur
"""

import discord
import random
import requests
import json
from words.words import *
from decouple import config


jokesUrl = r"https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"
quotesUrl = r"https://zenquotes.io/api/random"

def getJoke(url):
    r = requests.get(url)
    jsonData = json.loads(r.text)
    return jsonData

def getQuote(url):
    r = requests.get(url)
    jsonData = json.loads(r.text)
    return jsonData[0]['q'] + '\n - ' + jsonData[0]['a']

def matchwhole(content, list_to_match:list):
    return content in list_to_match

def matchstartswith(content, list_to_match:list):
    n1 = []
    n2 = []
    for i in list_to_match:
        c1 = content.startswith(i)              # Cheches if the content is present in the list
        n1.append(c1)
        
        c2 = content.startswith(i.capitalize()) # Capitalizes the item of the list and tries checkes again
        n2.append(c2)
    
    return any(n1) or any(n2)   # If one of them True, returns True else returns False

class BotClient(discord.Client):
    async def on_ready(self):
        print(f"[Info] Logged in as {self.user.name} {self.user.id}")
        print("___________________________________________")


    async def on_message(self, message):
        msg = message.content

        if not message.author.id == self.user.id:
            print(f"[INFO] A messege recived from {message.author.name} {message.author.id} - {msg}")

        elif message.author.id == self.user.id:
            print(f"[INFO] messege sent - {msg}")
            return                      # Make sure that the bot doesn't reply to itself


        if  matchwhole(msg, greetings_words):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(msg, special_grettings):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(msg, hello_to_bot):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(msg, health_question):
            await message.reply(random.choice(health_question_response))

        elif matchstartswith(msg, health_question_response):
            await message.reply(random.choice(health_question_response_reply))

        elif matchstartswith(msg, bot_question):
            await message.reply("Yes I am!")

        elif matchstartswith(msg, question_self_health):
            await message.reply("Oh! How are you? 😃")

        elif matchwhole(msg, too_like_pharse):
            await message.reply("Ooo")

        elif msg == "ping":
            await message.reply("pong", mention_author=True)

        elif matchstartswith(msg, some_random_words):
            await message.reply("Hey! 😀", mention_author=True)

        elif matchstartswith(msg, ["Is Mahin a dumb?", "is mahin a dumb?"]):
            await message.reply("Yes he is 🤣")

        elif matchstartswith(msg, ["Is Samin a dumb?", "is samin a dumb?"]):    # ME
            await message.reply("Aren't you a human? A human can tell this better.")

        elif matchstartswith(msg, making_sad_words):
            await message.reply("Ouch! 🥺")

        elif matchstartswith(msg, shutting_bot):
            await message.reply("Okay 🤐")
    
        elif matchstartswith(msg, thanking_words):
            await message.reply("Welcome!")

        elif matchstartswith(msg, fun_reaction):
            await message.reply(random.choice(fun_reaction_reply))

        elif message.content == "I'm from the east side of america":
            await message.reply(
                "Where we choose pride over character\nAnd we can pick sides, but this is us, this is us, this is")

        elif matchstartswith(msg, ["Who made you?", "who made you?", "Where are you from?"]):
            await message.channel.send("I'm a bot made by @sam.in#3588")

        elif matchstartswith(msg, [
            "!joke", "Tell a joke", "tell a joke", "Tell me a joke", "tell me a joke", "Joke please", "joke please"]):
            jsonJoke = getJoke(jokesUrl)
            jokeType = jsonJoke['type']
            setup = jsonJoke['setup']
            punchline = jsonJoke['punchline']
            await message.channel.send(f"**{jokeType}**\n{setup}\n{punchline}")

        elif matchstartswith(msg, telling_for_quotes):
            await message.channel.send(getQuote(quotesUrl))

        # else:                                         # Uncomment if you like    
        #    await message.reply("Sorry! cannot get that! 😶")



if __name__ == "__main__":
    x = config('TOKEN')
    client = BotClient()
    client.run(str(x))
