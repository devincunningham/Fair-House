import random

from discord.ext import commands
import discord


monke = discord.Client()


@monke.event
async def on_ready():
    test_channel = monke.get_channel(775175775644811264)
    await test_channel.send("Hello comrade.")


@monke.event
async def on_banana(message):
    if message.author == monke.user:
        return

    if 'banan' in message.content.lower():
        await message.channel.send(random.choice(['banana!', 'banan?!', 'mmmm,, banana!']))


monke.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
