import random

from discord.ext import commands
from datetime import datetime, timedelta

gorbotchev = commands.Bot(command_prefix='!')


@gorbotchev.event
async def on_ready():
    print("Hello comrade.")


@gorbotchev.command(aliases=['Solidarity'])
@commands.has_permissions(manage_messages=True)
async def solidarity(ctx):
    await ctx.send("Forever!")


@gorbotchev.event
async def on_message(message):
    if message.author == gorbotchev.user:
        return

    triggers = ['geetle', 'georgio']
    if any(trigger in message.content.lower() for trigger in triggers):
        if random.choice([True, False]):
            await message.channel.send('*Get that Geetle!*')

gorbotchev.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
