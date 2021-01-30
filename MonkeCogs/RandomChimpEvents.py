from discord.ext import commands
import discord
import random


class RandomChimpEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.test_channel = 775175775644811264
        self.cybermemes_channel = 753421717241725049

    @commands.Cog.listener()
    async def on_ready(self):
        test_channel = self.bot.get_channel(self.test_channel)
        print("monke online")
        # await test_channel.send("oooh oooh aaah aah!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        if message.channel == self.bot.get_channel(self.cybermemes_channel):
            if random.choice([True, False]):
                await message.add_reaction("<:laughmaker:767278745303384074>")

        if 'monke' in message.content.lower():
            print("Sending response.")
            await message.channel.send(random.choice(['monke! monke!!', 'aaahh! ooH?!']))
            await message.add_reaction("<:PogChimp:765315088344678440>")
            embed = discord.Embed(title="Random Chimp Event!", description="+1 Bananas!", color=0xffe852)
            await message.author.send(embed=embed)

        if 'banan' in message.content.lower():
            print("Sending response.")
            await message.channel.send(random.choice(['banana!', 'banan?!', 'mmmm,, banana!']))
            await message.add_reaction("<:PogChimp:765315088344678440>")

            embed = discord.Embed(title="Random Chimp Event!", description="-1 Bananas!", color=0xffe852)
            await message.author.send(embed=embed)
