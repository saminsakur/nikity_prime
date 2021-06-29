import discord
import random
import requests
import json
from decouple import config

greetings_words = [
    "What's up!", 
    "what's up!", 
    "whats up",
    "whats up!", 
    "Whats up!", 
    "What's up",
    "what' s up!",
    "What' s up!",
    "What' s up",
    "what' s up",
    "hello",
    "Hello",
    "hello!",
    "Hello!",
    "Hi",
    "Hi!",
    "hi", 
    "Sup", 
    "sup",
    "Sup!",
    "sup!",
    "Hey",
    "hey",
    "hey!",
    "Hey!",
    "Heyy",
    "Heyyy",
    "Heyyy!!!",
    "Heyyy!",
    "Heyy",
    "Heyy!",
    "Hey!!!",
    "Yo!",
    "yo!",
    "yo",
    "Yo",
    "Hello!",
    "Hey there!",
    "Hey!",
    "Sup", 
    "What's up!", 
    "Hey! 😃"
]

health_question = [
    "How are you?",
    "How are you doing?",
    "how are you?",
    "How are you",
    "how are you",
    "how are you doing?",
    "How do you do?",
    "how do you do?"
]

health_question_response = [
    "Fine!, how are you?",
    "Fine!",
    "I'm Fine! thanks!",
    "I'm fine!",
    "I'm fine! thank u",
    "I'm fine! thank you! 😃",
    "I'm fine! thank you!"
    "I'm fine",
    "I am fine!",
    "I am fine",
    "I'm well",
    "I'm well!",
    "I'm great!",
    "I'm great",
    "Fine! thank you! how are you?"
] 

health_question_response_reply = [
    "Nice you see",
    "Nice to know",
    "Great!"
]
thanking_words = [
    "Thank u",
    "thanks!", 
    "Thanks!",
    "Thanks",
    "thanks",
    "Thank u!", 
    "Thank you!", 
    "thank you!", 
    "thank you",
    "Thank you",
    "tq"
]

bot_question = [
    "Are you a bot?",
    "are you a bot?"
]

some_random_words = [
    "😀",
    "...",
    ".",
    "hehe"
]

making_sad_words = [
    "You are a dumb",
    "you are a dumb",
    "You are a dumb!",
    "you are a dumb"
    "You're a dumb!", 
    "you're a dumb!"
    "you're a dumb", 
    "You're a nonesense",
    "You are a nonesense"
]

def getJoke():
    r = requests.get(r"https://dad-jokes.p.rapidapi.com/random/joke")
    j = json.loads(r)
    return j

def matchwhole(content, list_to_match:list):
    for i in list_to_match:
        return i == content
 

def matchstartswith(content, list_to_match:list):
    return any(content.startswith(i) for i in list_to_match)

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

        elif any(message.content.startswith(i) for i in bot_question):
            await message.reply("Yes I am!")

        elif matchstartswith(msg, ["Ask me how I am", "Ask me how am I"]):
            await message.reply("How are you? 😃")

        elif message.content == "ping":
            await message.reply("pong", mention_author=True)

        elif matchstartswith(msg, some_random_words):
            await message.reply("Hey! 😀", mention_author=True)

        elif matchstartswith(msg, ["Is Mahin a dumb?", "is mahin a dumb?"]):
            await message.reply("Yes he is 🤣")

        elif matchstartswith(msg, making_sad_words):
            await message.reply("Ouch! 🥺")
    
        elif matchstartswith(msg, thanking_words):
            await message.reply("Welcome!")

        elif message.content == "I'm from the east side of america":
            await message.reply(
                "Where we choose pride over character\nAnd we can pick sides, but this is us, this is us, this is")

        elif matchstartswith(msg, ["Who made you?", "who made you?", "Where are you from?"]):
            await message.channel.send("I'm a bot made by @sam.in#3588")

        elif matchstartswith(msg, ["!joke", "Tell a joke", "tell a joke", "Tell me a joke", "tell me a joke", "Joke please"]):
            await message.channel.send(getJoke)

        # else:
        #    await message.reply("Sorry! cannot get that! 😶")


client = BotClient()
x = config('TOKEN')
client.run(str(x))
