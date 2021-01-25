from discord.ext import commands
import discord
import random


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wg_assignment_channel = 792886241099251712

        self.santa_cruz = 803074014767218688
        self.he_him = 803073599099502622
        self.she_her = 803073863965212682
        self.they_them = 803073964430590025
        self.any_pronouns = 803074276319690793
        self.film_club = 803074335606177802
        self.book_club = 763112475860008980
        self.music_makers = 772911718107578390
        self.dst_players = 803074526870110219

        # ID of reactions message in the Working Group Assignments channel.
        self.role_message_id = 803093966722433094
        self.emoji_to_role = {
            '🏄': self.santa_cruz,
            '💙': self.he_him,
            '💜': self.she_her,
            '💚': self.they_them,
            '🤍': self.any_pronouns,
            '🎧': self.music_makers,
            '🎥': self.film_club,
            '📚': self.book_club,
            '🍖': self.dst_players
        }

        self.roles_message = (
            "All the optional server roles can be added with this post! "
            'Just react with any combination of the following emoji:\n'
            ":blue_heart: = he/him\n"
            ":purple_heart: = she/her\n"
            ":green_heart: = they/them\n"
            ":white_heart: = any pronouns\n"
            ":person_surfing: = Santa Cruz (you'll be notified about local news and events)\n"
            ":books: = Book Club (you'll be notified about book club events)\n"
            ":movie_camera: = Film Club (you'll be notified about movie stuff)\n"
            ":headphones: = Music Makers (you'll be notified about music challenges, collabs, etc)\n"
            ":meat_on_bone: = Don't Starve Together (you'll be notified about Don't Starve Together game nights)"
        )

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_roles_message(self, ctx):
        await ctx.message.delete()
        await ctx.send(self.roles_message)
        last_message = ctx.channel.last_message_id
        message = await ctx.channel.fetch_message(int(last_message))
        for emoji in self.emoji_to_role.keys():
            await message.add_reaction(emoji)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_roles_message(self, ctx):
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(self.role_message_id)
        await message.edit(content=self.roles_message)
        for emoji in self.emoji_to_role.keys():
            await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Gives a role based on a reaction emoji."""

        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        try:
            print(f"{payload.member} role reacted with {payload.emoji.name}.")
            role_id = self.emoji_to_role[payload.emoji.name]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.bot.get_guild(payload.guild_id)
        role = guild.get_role(role_id)

        try:
            # Add the member to the working group role.
            print(f"Adding {payload.member} to {role}...")
            await payload.member.add_roles(role)
            print(f"Successfully added {payload.member} to {role}!")

            # Notifying the member with a direct message.
            embed = discord.Embed(
                title="Random Chimp Event!",
                description=f"You have been added to the **{role}** role.",
                color=0xffe852)
            embed.set_thumbnail(url="https://styles.redditmedia.com/t5_38svbo/styles/communityIcon_9qgbj03dhls51.png")
            await payload.member.send(embed=embed)
        except discord.HTTPException as e:
            print(e)
            # If we want to do something in case of errors we'd do it here.
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Removes a role based on a reaction emoji."""

        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji.name]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.bot.get_guild(payload.guild_id)
        role = guild.get_role(role_id)
        member = guild.get_member(payload.user_id)

        try:
            # Remove the member from the working group role.
            print(f"Removing {payload.user_id} from {role}...")
            await member.remove_roles(role)
            print(f"Successfully removed {payload.user_id} from {role}!")

            # Notifying the member with a direct message.
            embed = discord.Embed(
                title="Random Chimp Event!",
                description=f"You have been removed from the **{role}** role.",
                color=0xffe852)
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/3119912444/32e67236ee38f03fb9fa7e1cfd38b5c0.jpeg')
            await member.send(embed=embed)
        except discord.HTTPException as e:
            print(e)
            pass
