import os

from discord.ext import commands
import discord

from FairHouseBotCogs.RandomChimpEvents import RandomChimpEvents
from FairHouseBotCogs.Roles import Roles


intents = discord.Intents.default()
intents.members = True

monke = commands.Bot(command_prefix="!", intents=intents)
monke.add_cog(RandomChimpEvents(monke))
monke.add_cog(Roles(monke))
monke.run(os.environ['FAIRHOUSE_BOT_TOKEN'])
