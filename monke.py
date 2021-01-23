import random
from discord.ext import commands
import discord


class RandomChimpEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.test_channel = 775175775644811264

    @commands.Cog.listener()
    async def on_ready(self):
        test_channel = self.bot.get_channel(self.test_channel)
        await test_channel.send("oooh oooh aaah aah!")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.author.id)
        print(self.bot.user.id)
        if message.author.id == self.bot.user.id:
            print("Not responding to self.")
            return

        if 'banan' in message.content.lower():
            print("Sending response.")
            await message.channel.send(random.choice(['banana!', 'banan?!', 'mmmm,, banana!']))
            await message.add_reaction("<:PogChimp:765315088344678440>")

            embed = discord.Embed(title="A random event has occurred.", description="-1 Bananas!", color=0xffe852)
            await message.author.send(embed=embed)


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}'.format(member))
        else:
            await ctx.send('Hello **{0.name}**... This feels familiar.'.format(member))
        self._last_member = member


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.add_cog(RandomChimpEvents(bot))
bot.add_cog(Greetings(bot))
bot.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
