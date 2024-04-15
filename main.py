import os
import discord
from dotenv import load_dotenv
import asyncio
import base64

load_dotenv(".env")
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
channel = 1229165462290694276

# def encode(message):
#      return base64.b64encode(message.encode("utf-8"))
# def decode(message):
#      return base64.b64decode(message.decode("utf-8"))

def encode(s):
    return base64.b64encode(s.encode())

def decode(b):
    b = b.split('\'')[1]
    return base64.b64decode(b).decode()

async def send(message):
    channelobj = client.get_channel(channel)
    x = await channelobj.send(message)
    return x

async def fetch(id):
     channelobj = client.get_channel(channel)
     msg = await channelobj.fetch_message(id)
    #  print(msg)
     return decode(msg.content)

async def upload_file(filename):
    print("starting upload of")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channelobj = client.get_channel(channel)
    await channelobj.send(encode("DStore started!"))

@client.event
async def on_message(message):
    if message.author == client.user:
            return
    elif message.content.startswith("!fetch"):
         cmdInp = message.content.split(" ")
         msgId = cmdInp[1]
         await message.channel.send(await fetch(msgId))
    elif message.content.startswith("!encode"):
         cmdInp = message.content.split(" ")
         data = cmdInp[1]
         await message.channel.send(encode(data))
    elif message.content.startswith("!decode"):
         cmdInp = message.content.split(" ")
         data = cmdInp[1]
         await message.channel.send(decode(data))

client.run(token)