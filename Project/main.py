import discord
import requests
from discord.ext import commands

with open('token.txt', 'r') as f:
    ACCESS_TOKEN = f.readline()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# TODO: Add json link
# response = requests.get('<link>').json()

# Example
response = requests.get('https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json').json()

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f'We have logged in as {bot.user}')
    except Exception as e:
        print(e)

# TODO: Add your command
# @bot.tree.command(name='<指令名稱>', description='<指令敘述：說明指令功能>')
# async def <指令名稱>(interaction: discord.Interaction, msg: str):
#     指令操作...
#     await interaction.response.send_message("<傳送訊息>")
#     # INFO: 如果訊息量太大，需要拆分成多筆，那第二次訊息需要以底下方法傳送
#     await interaction.channel.send("<傳送訊息>")

# Example
@bot.tree.command(name='echo', description='傳入一個參數 msg，並回傳 msg 的內容')
async def echo(interaction: discord.Interaction, msg: str):
    await interaction.response.send_message(msg)

bot.run(ACCESS_TOKEN)
