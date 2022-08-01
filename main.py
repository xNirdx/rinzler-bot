# Imports
import discord.ext.commands
import logging

from bot import PyCordBot

# Set logging information
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Set intents
intents = discord.Intents.default()
intents.members = True

# Create the bot
bot = PyCordBot(intents=intents, debug_guilds=['674061350309330944'])

# Load cogs
bot.load_extension('cogs.rolemenu')

# Run the bot using its token
bot.run(bot.config['BOT']['token'])
