import discord
from discord import *
from discord.permissions import Permissions
import random

import io
import aiohttp
from io import BytesIO

async def respond_hello(message):
    await message.channel.send('Hello!')

async def print_sender_name(message):
    await message.channel.send(message.author)

async def print_count(message, bot):
    online = 0
    offline = 0
    idle = 0
    dnd = 0
    
    # for member in message.guild.members:
    for member in discord.utils.get(message.guild.members):
        print(member)
        if member.status is discord.Status.online:
            online += 1
        elif member.status is discord.Status.offline:
            offline += 1
        elif member.status is discord.Status.idle:
            idle += 1
        elif member.status is discord.Status.dnd:
            dnd += 1
    await message.channel.send(str(online) + " members are online, " + str(idle) + " members are idle, " + str(offline) + " members are off, " + str(dnd) + " members are in Do not disturb mode")

async def make_admin(message):
    await message.channel.send("I just made you an admin !")
    await message.author.server_permissions
    # await guild.message.author.setPermissions([Permissions.FLAGS.ADMINISTRATOR])

async def random_comic(message):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://c.xkcd.com/random/comic/") as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            # with open(data) as f:
            #     picture=discord.File(f)
            await message.channel.send(file=discord.File(data, 'cool_image.png'))
    # await message.channel.send(random.choice())