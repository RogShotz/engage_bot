import discord
from discord import app_commands
from discord.ext import commands
import asyncio


class RoleGiverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="send_roles", description="Sends lists of roles")
    @app_commands.default_permissions(administrator=True)
    async def send_roles(self, itx: discord.Interaction):
        msg = ""
        for role in itx.guild.roles[1:]:  # skips @everyone
            if role.permissions.administrator or role.permissions.manage_roles:
                msg += f"**{role} - Restricted**\n"
            else:
                msg += f"**{role}**\n"
        await itx.response.send_message(msg)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            return
        await asyncio.sleep(3)
        channel = discord.utils.get(message.guild.channels, name='roles')
        if message.channel != channel:
            return
        # make sure its not the bot and not send_message response
        if message.author.bot and message.guild.roles[1].name not in message.content:
            await message.delete()
            return
        roles = message.guild.roles
        for role in roles:
            if role.name.lower() == message.content.lower():
                if role.permissions.administrator or role.permissions.manage_roles:
                    await message.author.send(f"Role `{role.name}` is admin restricted in {message.guild.name} server, ask an admin to give you this role if you have permission.")
                    await message.delete()
                    return
                elif message.author.get_role(role.id):
                    await message.author.remove_roles(role)
                    await message.author.send(f"Removed role `{role.name}` from you in {message.guild.name} server")
                    await message.delete()
                    return
                else:
                    await message.author.add_roles(role)
                    await message.author.send(f"Gave role `{role.name}` to you in {message.guild.name} server")
                    await message.delete()
                    return

        await message.author.send(f"No role `{message.content}` in {message.guild.name} server")
        await message.delete()


async def setup(bot):  # set async function
    await bot.add_cog(RoleGiverCog(bot))  # Use await
