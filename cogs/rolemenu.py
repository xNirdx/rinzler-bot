# Imports
import discord
import discord.ext.commands
import configparser

# Set the path to the config file
CONFIG_PATH = '../config.ini'


# RoleMenu cog for handling the role menu
class RoleMenu(discord.ext.commands.Cog):
    def __init__(self, bot):
        # Pass the bot to our cog
        self.bot = bot

        # Set our config file and read it
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)

    # Slash command to add a role to the role menu
    @discord.slash_command(guild_ids=['674061350309330944'])
    async def add_role(self, ctx, role: discord.SlashCommandOptionType.role):
        """Say hello!"""

        converter = discord.ext.commands.RoleConverter()
        r = await converter.convert(ctx, role)

        await ctx.respond(f"You chose the {r.name} role")


def setup(bot):
    bot.add_cog(RoleMenu(bot))
