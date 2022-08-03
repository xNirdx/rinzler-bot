# Imports
import discord.ext.commands
import configparser

from discord import slash_command
from views.rolemenu import category_select


# RoleMenu cog for handling the role menu
class RoleMenu(discord.ext.commands.Cog):
    def __init__(self, bot):
        # Pass the bot to our cog
        self.bot = bot

        # Set our config file and read it
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    # Slash command to add a role to the role menu
    @slash_command(guild_ids=['674061350309330944'])
    async def add_role(self, ctx, role: discord.Option(discord.Role)):
        """Say hello!"""

        view = category_select.CategorySelect(bot=self.bot, role=role)

        await ctx.respond(
            f"Please select a role group for {role.mention}:",
            view=view
        )


def setup(bot):
    bot.add_cog(RoleMenu(bot))
