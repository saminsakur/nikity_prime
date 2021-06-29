import discord
import random
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
    "Hey 😃"
]

health_question = [
    "How are you?",
    "How are you doing?",
    "how are you?",
    "how are you doing?"
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
    "I am fine"
    "Fine! thank you! how are you?"
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


        if  message.content in greetings_words:
            await message.reply(greetings_words[random.randint(0, len(greetings_words) -1)])

        elif message.content in health_question:
            await message.reply(health_question_response[random.randint(0, len(health_question_response) -1)])

        elif message.content in health_question_response:
            await message.reply("Nice you see")

        elif message.content == "ping":
            await message.reply("pong", mention_author=True)

        elif any([message.content.startswith(i) for i in thanking_words]):
            await message.reply("Welcome!")

        elif message.content == "I'm from the east side of america":
            await message.reply(
                "Where we choose pride over character\nAnd we can pick sides, but this is us, this is us, this is")

        elif message.content.startswith("Who are you?"):
            await message.channel.send("I'm a bot made by @sam.in#3588")

        else:
            await message.reply("Sorry! cannot get that! 😶")

client = BotClient()
x = config('TOKEN')
client.run(str(x))
