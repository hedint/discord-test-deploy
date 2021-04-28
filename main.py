import discord
from dotenv import load_dotenv
import os
import requests

load_dotenv()
TOKEN = "ODI4Mzg2NjI1NTc4NDY3Mzc5.YGo1Kg.uPTmfTkZFKK9XigoGKZ4hcIOcX8"


def get_cat():
    result = requests.get("https://api.thecatapi.com/v1/images/search").json()
    return result[0]['url']


def get_dog():
    result = requests.get("https://dog.ceo/api/breeds/image/random").json()
    return result['message']


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'Бот готов')
        for guild in self.guilds:
            print(
                f'{client.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})'
            )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.lower() in ["кот", "котец", "котик", "котель", "кошка"]:
            await message.channel.send(get_cat())
        elif message.content.lower() in ["пес", "песель", "собака"]:
            await message.channel.send(get_dog())
        else:
            await message.channel.send("Я здесь чтобы показывать котиков и песиков!")


client = YLBotClient()
client.run(TOKEN)
