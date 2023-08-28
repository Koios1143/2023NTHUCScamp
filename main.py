import yaml
import discord

ConfigYAML = yaml.safe_load(open('./config.yml', 'r').read())
ACCESS_TOKEN = ConfigYAML['ACCESS_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    print('User "{}" send a message {}'.format(
        message.author.name,
        message.content
    ))
    await message.channel.send(message.content)

client.run(ACCESS_TOKEN)