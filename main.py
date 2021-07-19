"""
    ----------------
    | NIKITY PRIME |
    ----------------
    A discord bot

    Author - Samin Sakur
"""

import discord
import random
import os
import re
import requests
import json
from words.words import *
from decouple import config
from boto.s3.connection import S3Connection
import run

jokesUrl = r"https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"
quotesUrl = r"https://zenquotes.io/api/random"

mention = f'<@!858740782503952384>'

mention_pattern = re.compile(r"^<@!858740782503952384>+[^\s]+.+")
mentionspace_pattern = re.compile(r"^<@!858740782503952384>+\s+.+")


def getJoke(url):
    r = requests.get(url)
    jsonData = json.loads(r.text)
    return jsonData


def getQuote(url):
    r = requests.get(url)
    jsonData = json.loads(r.text)
    return jsonData[0]['q'] + '\n - ' + jsonData[0]['a']


def matchwhole(content, list_to_match: list):
    return content in list_to_match


def matcheachwrd(content, list_to_match):
    x = any([i in content for i in list_to_match])
    y = any([i.capitalize() in content for i in list_to_match])
    return x or y


def matchstartswith(message, content, list_to_match: list):
    mentionspace = mention + " "

    if client.user.mentioned_in(message):
        if mention_pattern.search(content):
            x = content.replace(mention, "")
            n1 = []
            n2 = []
            n3 = []
            for i in list_to_match:
                c1 = x.startswith(i)  # Cheches if the content is present in the list
                n1.append(c1)

                c2 = x.startswith(i.capitalize())  # Capitalizes the item of the list and tries checkes again
                n2.append(c2)

                c3 = x.startswith(i.upper())
                n3.append(c3)

            return any(n1) or any(n2) or any(n3)  # If one of them True, returns True else returns False

        if mentionspace_pattern.search(content):
            y = content.replace(mentionspace, "")
            n1 = []
            n2 = []
            n3 = []
            for i in list_to_match:
                c1 = y.startswith(i)  # Cheches if the content is present in the list
                n1.append(c1)

                c2 = y.startswith(i.capitalize())  # Capitalizes the item of the list and tries checkes again
                n2.append(c2)

                c3 = y.startswith(i.upper())
                n3.append(c3)

            return any(n1) or any(n2) or any(n3)  # If one of them True, returns True else returns False


    else:
        n1 = []
        n2 = []
        n3 = []
        for i in list_to_match:
            c1 = content.startswith(i)  # Checkes if the content is present in the list
            n1.append(c1)

            c2 = content.startswith(i.capitalize())  # Capitalizes the item of the list and tries checkes again
            n2.append(c2)

            c3 = content.startswith(i.upper())
            n3.append(c3)

        return any(n1) or any(n2) or any(n3)  # If one of them True, returns True else returns False


class BotClient(discord.Client):
    async def on_ready(self):
        print(f"[INFO] Logged in as {self.user.name} {self.user.id}")
        print("___________________________________________")

    async def on_message(self, message):
        msg = message.content

        if message.author.id != self.user.id:
            print(f"[INFO] A messege recived from {message.author.name} {message.author.id} - {msg}")

        if message.author.id == self.user.id:
            print(f"[INFO] messege sent - {msg}")
            return  # Make sure that the bot doesn't reply to itself

        if matchwhole(msg, greetings_words):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(message, msg, special_grettings):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(message, msg, hello_to_bot):
            await message.reply(random.choice(greetings_words))

        elif matchstartswith(message, msg, health_question):
            await message.reply(random.choice(health_question_response))

        elif matchstartswith(message, msg, health_question_response):
            await message.reply(random.choice(health_question_response_reply))

        elif matchstartswith(message, msg, bot_question):
            await message.reply("Yes I am!")

        elif matchstartswith(message, msg, question_self_health):
            await message.reply("Oh! How are you? 😃")

        elif matchwhole(msg, too_like_pharse):
            await message.reply("Ooo")

        elif msg == "ping":
            await message.reply("pong", mention_author=True)

        elif matchstartswith(message, msg, some_random_words):
            await message.reply("Hey! 😀", mention_author=True)

        elif matchstartswith(message, msg, ["Is Mahin a dumb?", "is mahin a dumb?"]):
            await message.reply("Yes he is 🤣")

        elif matchstartswith(message, msg, ["Is Samin a dumb?", "is samin a dumb?"]):  # ME
            await message.reply("Aren't you a human? A human can tell this better.")

        elif matchstartswith(message, msg, making_sad_words):
            await message.reply("Ouch! 🥺")

        elif matcheachwrd(msg, shutting_bot):
            await message.reply("Okay 🤐")

        elif matchstartswith(message, msg, thanking_words):
            await message.reply("Welcome!")

        elif matchstartswith(message, msg, fun_reaction):
            await message.reply(random.choice(fun_reaction_reply))

        elif message.content == "I'm from the east side of america":
            await message.reply(
                "Where we choose pride over character\nAnd we can pick sides, but this is us, this is us, this is")

        elif matchstartswith(message, msg, ["Who made you?", "who made you?", "Where are you from?"]):
            await message.channel.send("I'm a bot made by @sam.in#3588")

        elif matchstartswith(message, msg, askingforjoke):
            jsonJoke = getJoke(jokesUrl)
            jokeType = jsonJoke['type']
            setup = jsonJoke['setup']
            punchline = jsonJoke['punchline']
            await message.channel.send(f"**{jokeType}**\n{setup}\n{punchline}")

        elif matchstartswith(message, msg, telling_for_quotes):
            await message.channel.send(getQuote(quotesUrl))

        elif matchstartswith(message, msg, nice_words):
            await message.reply(random.choice(health_question_response_reply))

        elif matcheachwrd(msg, ["Good"]):
            await message.reply(random.choice(health_question_response_reply))

        elif matchstartswith(message, msg, ["wow"]):
            await message.reply("😃")

        # else:                                                    # Uncomment if you like    
        #    await message.reply("Sorry! cannot get that! 😶")


if __name__ == "__main__":
    x = S3Connection(os.environ['TOKEN'])
    run.keep_running()
    client = BotClient()
    client.run(str(x))
