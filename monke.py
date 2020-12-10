import random

from discord.ext import commands

monke = commands.Bot(command_prefix='!')


@monke.event
async def on_ready():
    print("Hello comrade.")


@monke.command(aliases=['Solidarity'])
@commands.has_permissions(manage_messages=True)
async def solidarity(ctx):
    await ctx.send("Forever!")


@monke.event
async def on_message(message):
    if message.author == monke.user:
        return

    triggers = ['geetle', 'georgio']
    if any(trigger in message.content.lower() for trigger in triggers):
        if random.choice([True, False]):
            await message.channel.send('*Get that Geetle!*')

monke.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
