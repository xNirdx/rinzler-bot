# Imports
import discord
import configparser


# Our own subclass of the discord.Bot class to implement our own features
class PyCordBot(discord.Bot):
    # Constructor
    def __init__(self, *args, **options):
        # Don't forget to call the parent constructor as well
        super().__init__(*args, **options)

        # Read the bot's config file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    # Emits when the bot is ready
    async def on_ready(self):
        """Emits when the bot is ready"""

        print(f"{self.user.name} running!")

    # Emits when a user joins the server
    async def on_member_join(self, member):
        """Emits when a member joins the server"""

        welcome_channel = await self.fetch_channel(int(self.config['CHANNELS']['welcome']))
        await welcome_channel.send(f"Thank you for joining the server, <@{member.id}>")
