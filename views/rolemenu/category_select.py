# Imports
import discord


class SelectMenu(discord.ui.Select):
    def __init__(self, bot, role):
        super().__init__()

        self.placeholder = "Choose a role category"
        self.min_values = 1
        self.max_values = 1
        self.options = []
        self.bot = bot
        self.role = role

        self.role_groups = self.bot.database.get_role_groups()

        for group in self.role_groups:
            group_name = group[1]
            group_value = f"{group_name} {str(group[0])}"

            self.options.append(
                discord.SelectOption(label=group_name, value=group_value)
            )

    async def callback(self, interaction: discord.Interaction):
        role_group = interaction.data['values'][0]
        group_name = role_group[:role_group.rfind(' ')]
        group_id = int(role_group[role_group.rfind(' '):])

        await self.bot.database.add_role(role=self.role, group_id=group_id)
        await interaction.response.send_message(f"{self.role.mention} has been added to `{group_name}`.")


class CategorySelect(discord.ui.View):
    def __init__(self, *items: discord.ui.Item, bot, role):
        super().__init__(*items)

        self.add_item(SelectMenu(bot=bot, role=role))
