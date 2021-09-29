import os
import discord
import random

from discord.ext import commands
from discord.ext.commands import Bot

from todos import *

token = "ODkyODIyMDQ2NTE2NjA5MTA0.YVSfUw.p7cs9wHVSBwRisEByuYeDOCyhiM"


bot = commands.Bot(
    command_prefix='!',  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 'Yann#3484'  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!name"):
        await print_sender_name(message)
    
    if message.content.startswith("!count"):
        await print_count(message, bot)

    if message.content.startswith("!admin"):
        await make_admin(message)

    if message.content.startswith("!xkcd"):
        await random_comic(message)

# @bot.command(name='name')
# async def print_server(context):
# 	guild = context.guild
	
# 	await context.send(f'Server Name: {guild.name}')
# 	await context.send(f'Server Size: {len(guild.members)}')
# 	await context.send(f'Server Name: {guild.owner.display_name}')

# bot.run(token)

bot.run(token)  # Starts the bot

