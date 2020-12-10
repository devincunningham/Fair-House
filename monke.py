import random
import discord


monke = discord.Client()


@monke.event
async def on_ready():
    test_channel = monke.get_channel(775175775644811264)
    await test_channel.send("oooh oooh aaah aah!")


@monke.event
async def on_message(message):
    if message.author == monke.user:
        return

    if 'banan' in message.content.lower():
        await message.channel.send(random.choice(['banana!', 'banan?!', 'mmmm,, banana!']))
        await message.add_reaction("<:PogChimp:765315088344678440>")


monke.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
