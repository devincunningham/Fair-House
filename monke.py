import os
import random
import discord


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.test_channel = 775175775644811264

    async def on_ready(self):
        test_channel = client.get_channel(self.test_channel)
        await test_channel.send("oooh oooh aaah aah!")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if 'banan' in message.content.lower():
            await message.channel.send(random.choice(['banana!', 'banan?!', 'mmmm,, banana!']))
            await message.add_reaction("<:PogChimp:765315088344678440>")

            embed = discord.Embed(title="A random event has occurred.", description="-1 Bananas!", color=0xffe852)
            await message.member.send(embed=embed)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
