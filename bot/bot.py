from dotenv import load_dotenv
load_dotenv()
import os
import io
import discord
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    json_data = json.loads(response.text)
    cat_url = json_data[0]['url']
    return cat_url

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content.startswith('$cat'):
            cat_url = get_cat()
            response = requests.get(cat_url, stream=True)
            await message.channel.send(file=discord.File(io.BytesIO(response.content), 'cat.png'))
        elif message.content.startswith('$hi'):
            await message.channel.send('Hey bestie!')
        elif message.content.startswith('$howdy'):
            await message.channel.send('howdy partner!🤠')
        elif message.content.startswith('$bye'):
            await message.channel.send('Ciao!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))