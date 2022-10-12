import discord
import os
from discord.ext import commands
import json

GUILD = os.getenv('DISCORD_GUILD')
PATH = os.getcwd() + "/cogs/levels/"


class LevelsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()  # TODO: MAKE FUNCTIONAL
    async def on_member_join(self, member):
        with open(r"users.json", 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

    @commands.Cog.listener()
    async def on_message(self, message):
        with open(PATH + "levels.json", 'r') as f:
            ids = json.load(f)

        await self.update_data(ids, message.author.id)
        await self.add_experience(ids, message.author.id, 5)
        await self.level_up(ids, message.author, message)

        with open(PATH + 'levels.json', 'w') as f:
            json.dump(ids, f, indent=4)

    async def update_data(self, ids, user):
        id = ids.get(str(user))
        if not id:
            print("Adding USR to DB")
            ids[str(user)] = {"experience": 0, "level": 0}

    async def add_experience(self, ids, user, exp):
        ids[str(user)]["experience"] += 5

    async def level_up(self, ids, user, message):
        experience = ids[str(user.id)]["experience"]
        lvl_start = ids[str(user.id)]["level"]
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            desc = ""
            if message.author.bot == False:
                desc = f'{user.mention} has leveled up to level {lvl_end}! :fire: 'f'\n Great job,{user.mention} '
            else:
                desc = f'Your {user.mention} has leveled up to level {lvl_end}! :fire: 'f'\n {user.mention} The Best Bot In Town <3 '
            embed = discord.Embed(title="**LEVEL UP!**",
                                  description=desc,
                                  color=discord.Color.dark_red())
            try:  # try to see if it has avatar, if not set default
                embed.set_thumbnail(url=user.avatar.url)
            except:
                # TODO: MAKE IT BOT ICON URL
                embed.set_thumbnail(
                    url="https://webstockreview.net/images/discord-icon-png.png")
            ids[str(user.id)]["level"] = lvl_end
            await message.channel.send(embed=embed)


async def setup(bot):  # set async function
    await bot.add_cog(LevelsCog(bot))  # Use await
