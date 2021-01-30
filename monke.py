from discord.ext import commands
import discord

from MonkeCogs.RandomChimpEvents import RandomChimpEvents
from MonkeCogs.Roles import Roles


intents = discord.Intents.default()
intents.members = True

monke = commands.Bot(command_prefix="!", intents=intents)
monke.add_cog(RandomChimpEvents(monke))
monke.add_cog(Roles(monke))
monke.run('Nzc1MTcyMTI3MTg2ODc4NDc0.X6idTQ.toLVXhf3pMvho5XsNaN1JLRImgY')
