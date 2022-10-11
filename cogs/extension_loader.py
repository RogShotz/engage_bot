import io
import traceback
import discord
from discord.ext import commands


class ExtLoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # nice to have, allows bot to always run
    @commands.command(name="reload_ext", description="Reloads specified extension")
    @commands.has_guild_permissions(administrator=True)
    async def reload_ext(self, ctx, ext):
        await self.bot.reload_extension(ext)
        await ctx.channel.send(f"Reload Finished on EXT: {ctx.author.mention}")

    @commands.command(name="load_ext", description="Loads new specified extension")
    @commands.has_guild_permissions(administrator=True)
    async def load_ext(self, ctx, ext):
        await self.bot.load_extension(ext)
        await ctx.channel.send(f"Load Finished on EXT: {ext} {ctx.author.mention}")

    @commands.command(name="unload_ext", description="Unoads specified extension")
    @commands.has_guild_permissions(administrator=True)
    async def unload_ext(self, ctx, ext):
        await self.bot.unload_extension(ext)
        await ctx.channel.send(f"Unload Finished on EXT: {ext} {ctx.author.mention}")

    async def cog_command_error(self, ctx, error):
        cogs = '```\n'
        for cog in self.bot.extensions.keys():
            cogs += cog + "\n"
        cogs += '```'
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await ctx.channel.send(f"No EXT inputted: {ctx.author.mention}\n\nHere is a list of avaliable extensions:\n {cogs}")
            return
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            error = error.original
            msg_arr = ctx.message.content.split()
            ext = msg_arr[1]

            if isinstance(error, discord.ext.commands.ExtensionNotFound) or isinstance(error, discord.ext.commands.ExtensionNotLoaded):
                await ctx.channel.send(f"NO SUCH EXTENSION FOUND: {ext}, {ctx.author.mention}\n\nHere is a list of avaliable extensions:\n{cogs}")
            elif isinstance(error, discord.ext.commands.ExtensionAlreadyLoaded):
                await ctx.channel.send(f"EXTENSION ALREADY LOADED: {ext}, {ctx.author.mention}")
            elif isinstance(error, commands.NoEntryPointError):
                await ctx.channel.send(f"EXTENSION HAS NO ENTRY POINT: {ext}, {ctx.author.mention}")
            elif isinstance(error, discord.ext.commands.ExtensionFailed):
                # sends tracenack
                buff = io.StringIO()
                error = getattr(error, 'original', error)

                traceback.print_exception(
                    type(error), error, error.__traceback__, file=buff)

                buff.seek(0)  # Back to start
                paginator = commands.Paginator()
                for line in buff:
                    paginator.add_line(line)
                await ctx.send(f"EXTENSION, {ext}, HAS AN ERROR: {ctx.author.mention}")
                for page in paginator.pages:
                    await ctx.send(page)


async def setup(bot):  # set async function
    await bot.add_cog(ExtLoaderCog(bot))  # Use await
