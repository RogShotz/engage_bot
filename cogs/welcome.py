import discord
from discord import ui, app_commands
from discord.ui import Button, View
from discord.ext import commands
from datetime import datetime
from discord.utils import get


class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="welcome_message")
    async def welcome_message(self, ctx):
        self.bot.dispatch('member_join', ctx.author)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # embed image for welcome
        embed = discord.Embed(
            title=f"Welcome to Engage!", color=0x00ffee, description=f"Everyone welcome {member.mention}")
        embed.set_footer(text="Glad to have you here :)")
        channel = self.bot.get_channel(1029568286553292900)
        await channel.send(embed=embed)
        # TODO: MAKE BETTER
        embed = discord.Embed(
            title=f"Welcome Message", color=0x00FF00, timestamp=datetime.now())
        embed.add_field(
            name="User", value=member, inline=False)
        embed.add_field(
            name="Disclaimer", value="Welcome to the server!\nThis discord bot logs server infractions and records levels.\nFuture logging updates may occur.\nWe hope you enjoy the server.", inline=False)
        await member.send(embed=embed)


async def setup(bot):  # set async function
    await bot.add_cog(WelcomeCog(bot))  # use await
