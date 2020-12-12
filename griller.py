import random
import discord


griller = discord.Client()


@griller.event
async def on_ready():
    test_channel = griller.get_channel(775175775644811264)
    await test_channel.send("ooOOhh OOh ooUuh!")


@griller.event
async def on_message(message):
    if message.author == griller.user:
        return

    if 'banan' in message.content.lower():
        await message.channel.send(random.choice(['OOhh OOH!', 'aoh aoh AOh!!']))
        await message.add_reaction("<:PogChimp:765315088344678440>")


griller.run('Nzg3MTQ4MTcwMTE0NjI5NjY1.X9Qu3A.habXmFwz0xBEdcZYZGgf5c3yh84')
