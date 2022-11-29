
from discord.ext.commands   import Cog


class Base(Cog):
    def __init__(self, bot):
        self.bot = bot
        # print('init base cog')

    @Cog.listener()
    async def on_message(self, message):
        print(f'{message.author} (cogs.base)\n=> {message.content}\n')
        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(Base(bot))
