import discord
from dotenv import load_dotenv
import requests
import os
load_dotenv()
TOKEN = os.environ.get("TOKEN")
import logging
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def get_cat():
    logger.error("GET CAT")
    result = requests.get("https://api.thecatapi.com/v1/images/search").json()
    return result[0]['url']


def get_dog():
    logger.error("GET DOG")

    result = requests.get("https://dog.ceo/api/breeds/image/random").json()
    return result['message']


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.error("ON READY")
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
logger.error("START BOT")
logger.error(TOKEN)

client.run(TOKEN)
