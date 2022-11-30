
from discord.ext.commands   import Cog, command


class Base(Cog):
    prefixes = ['/', '!', '.', '?']

    def __init__(self, bot):
        # print('init base cog')
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        await print(f'{message.author} (cogs.base)\n=> {message.content}\n')
    #     await self.bot.process_commands(message)

    @command(
        aliases = [ f'{prefix}ping' for prefix in prefixes ]
    )
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(round(self.bot.latency, 4) * 1000)}ms')


async def setup(bot):
    await bot.add_cog(Base(bot))
