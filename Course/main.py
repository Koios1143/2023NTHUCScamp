import discord
import requests
from discord.ext import commands

with open('token.txt', 'r') as f:
    ACCESS_TOKEN = f.readline()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

response = requests.get('https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json').json()

searched_course = []
selected_course = []

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f'We have logged in as {bot.user}.')
    except Exception as e:
        print(e)

def generate_course_string(course):
    return f'**{course["課程中文名稱"]}** ({course["教室與上課時間"].split()[-1] if course["教室與上課時間"] else ""})'

@bot.tree.command(name='search_dept', description='輸入一個參數 dept 代表系所代號，列出該系所的所有課程')
async def search_dept(interaction: discord.Interaction, dept: str):
    dept_course = [i for i in response if dept in i['科號']]
    await interaction.response.send_message(f'{dept} 系所開設的課程：\n')
    if not dept_course:
        return
    send_msg = ''
    for i, c in enumerate(dept_course, 1):
        send_msg += f'{i}. {generate_course_string(c)}\n'
        if i % 20 == 0 and len(dept_course) > i:
            await interaction.channel.send(f'{send_msg}')
            send_msg = ''
    await interaction.channel.send(f'{send_msg}')
    global searched_course
    searched_course = dept_course


@bot.tree.command(name='search_course', description='輸入一個參數 course 來搜尋課程')
async def search_course(interaction: discord.Interaction, course: str):
    search_course = [i for i in response if course in i['課程中文名稱']]
    await interaction.response.send_message(f'符合「{course}」的結果：\n')
    if not search_course:
        return
    send_msg = ''
    for i, c in enumerate(search_course, 1):
        send_msg += f'{i}. {generate_course_string(c)}\n'
        if i == 20 and len(search_course) > 50:
            await interaction.channel.send(f'{send_msg}')
            send_msg = ''
    await interaction.channel.send(f'{send_msg}')
    global searched_course
    searched_course = search_course

@bot.tree.command(name='select_course', description='輸入一個編號 x 來選擇課程')
async def select_course(interaction: discord.Interaction, x: int):
    if not searched_course:
        return await interaction.response.send_message(f'請先搜尋課程')
    elif not 0 < x <= len(searched_course):
        return await interaction.response.send_message(f'請輸入範圍內的編號')
    await interaction.response.send_message(f'選擇了「{generate_course_string(searched_course[x-1])}」')
    global selected_course
    selected_course.append(searched_course[x-1])

@bot.tree.command(name='list_course', description='列出所有已選的課程')
async def list_course(interaction: discord.Interaction):
    await interaction.response.send_message(f'目前選擇的課程：\n')
    if not selected_course:
        return
    send_msg = ''
    for i, c in enumerate(selected_course, 1):
        send_msg += f'{i}. {generate_course_string(c)}\n'
        if i == 20 and len(search_course) > 50:
            await interaction.channel.send(f'{send_msg}')
            send_msg = ''
    await interaction.channel.send(f'{send_msg}')

bot.run(ACCESS_TOKEN)