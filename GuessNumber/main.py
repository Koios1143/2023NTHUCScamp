import random

import discord
from discord.ext import commands

with open("token.txt", 'r') as f:
    ACCESS_TOKEN = f.readline()

# Create a bot
# Represents a bot connection that connects to Discord.
bot = commands.Bot(['/'], intents=discord.Intents.all())
target = -1


# When the bot has successfully logged in to the server, on_ready() will be triggered.
@bot.event
async def on_ready():
    print(f"We have logged in as `{bot.user}`!!")


# Handle start command
@bot.command()
async def start(ctx: commands.Context, arg: str):
    global target
    assert (n := int(arg)) > 0
    target = random.randint(1, n)
    print(f"{ctx.author} start a new game with answer being {target}!!")
    await ctx.send(f"{ctx.author} start a new game with the closed interval [1, {arg}]!!")


# Handle guess command
@bot.command()
async def guess(ctx: commands.Context, arg: str):
    global target
    if target < 0:
        return await ctx.send("Please start a new game first!!")
    if target == int(arg):
        target = -1
        await ctx.send("Bingo!!")
    else:
        await ctx.send("Wrong answer QQ")


# Run the Discord BOT
if __name__ == "__main__":
    bot.run(ACCESS_TOKEN)
