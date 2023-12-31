# 2023 NTHU CS camp Discord BOT

Here are the [preview notes](https://hackmd.io/@Koios/2023CScamp/) and the [slides](https://drive.google.com/drive/folders/1e4hxxbM7dwhdbe1i_YKJuSzMD2E1vErn).

This is a repository of 2023 NTHU CS camp. During the lecture, we'll have four different BOT examples, including
- Parrot Bot
  -  A simple DC BOT that will always send the same message content as what user sent.
- Role Bot
  -  A simple DC BOT that can add role to user with reaction being triggered.
- Guess Number Bot
  -  A simple DC BOT that can play "guess number" with user.
- Wordle Bot
  -  A DC BOT that implement wordle game.

## Setup

```bash
pip3 install discord.py
```

## Usage

```bash
cd <example>
echo <token> > token.txt
python3 main.py
```

## Note

Every BOT will contain a `token.txt`, you should put your BOT token into this file.

> IF YOU WANT TO PUSH YOUR BOT TO GITHUB, DO NOT FORGET TO IGNORE `token.txt`!!

Whenever you want to implement a new functionality that you don't know how to implement, try to read [discord.py documents](https://discordpy.readthedocs.io/en/stable/index.html) first. Sometimes you'll have to google it, to find out all information that spread in the whole internet.

ChatGPT might be a good tool to give you some insights and advice!