import io
import traceback
import discord
from discord.ext import commands

PATH = "cogs."  # global var so you don't have to type cogs. every time


class SyncCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # nice to have, allows bot to always run
    @commands.command(name="sync", description="Syncs commands")
    @commands.has_guild_permissions(administrator=True)
    async def reload_ext(self, ctx):
        synced = await ctx.bot.tree.sync(guild=ctx.guild)

        await ctx.channel.send(f"Sync finished {ctx.author.mention}")


async def setup(bot):  # set async function
    await bot.add_cog(SyncCog(bot))  # Use await
