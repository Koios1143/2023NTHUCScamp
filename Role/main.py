import discord
from discord.utils import get

ACCESS_TOKEN = open('token.txt', 'r').read()

# Intents are bitwise values, identifying which correlate to a set of related events.
# Set all for convenience.
intents = discord.Intents.all()

# Create a client
# Represents a client connection that connects to Discord.
client = discord.Client(intents=intents)

# When the bot has successfully logged in to the server, on_ready() will be triggered.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# When client send message, on_message() will be triggered.
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_message#discord.on_message
@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    print('User "{}" send a message {}'.format(
        message.author.name,
        message.content
    ))
    await message.channel.send(message.content)

# When client add reaction, on_raw_reaction_add() will be triggered
# We use "on_raw_reaction_add" instead of "on_reaction_add" to get the "member" attribute
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_raw_reaction#discord.on_raw_reaction_add
@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    print('Receive reaction {}\tSend by {}'.format(payload.emoji, payload.member.name))
    
    # guild here means "server" in DC
    # Know which guild we're in, and figure out all roles in that guild
    guild = client.get_guild(payload.guild_id)
    # Then get the role with name "Test"
    role = get(guild.roles, name='Test')

    # Add role to the member
    await payload.member.add_roles(role)
    # Send notification message
    await client.get_channel(payload.channel_id).send('成功新增 <@&{}> 給 <@!{}>'.format(role.id, payload.user_id))

# Run the Discord BOT
if __name__ == '__main__':
    client.run(ACCESS_TOKEN)