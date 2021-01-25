import random
from discord.ext import commands
import discord

from RandomChimpEvents import RandomChimpEvents
from Roles import Roles


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

monke = commands.Bot(command_prefix="!", intents=intents)
monke.add_cog(RandomChimpEvents(monke))
monke.add_cog(Roles(monke))
monke.add_cog(Greetings(monke))
monke.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
