# Imports
import discord
import asyncio

from db import DB


def build_options(categories):
    options = []

    for category in categories:
        options.append(
            discord.SelectOption(
                label=category,
                emoji='👽'
            )
        )

    return options


class SelectMenu(discord.ui.Select):
    def __init__(self, categories):
        super().__init__()

        self.placeholder = "Choose a role category"
        self.min_values = 1
        self.max_values = 1

        for category in categories:
            self.options.append(discord.SelectOption(label=category, emoji='👽'))

    async def callback(self, interaction: discord.Interaction):
        # db = DB()
        # await db.add_role()
        category = interaction.data['values'][0]

        await interaction.response.send_message(f"You chose the {category} category")


class CategorySelect(discord.ui.View):
    def __init__(self, *items: discord.ui.Item, categories):
        super().__init__(*items)

        self.categories = categories
        self.add_item(SelectMenu(categories=self.categories))
