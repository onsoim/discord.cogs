
from discord.ext.commands   import Cog

import re


class YouTube(Cog):
    def __init__(self, bot):
        print('init youtube cog')
        self.bot    = bot
        self.re     = {
            'url': '(?:https?:\\/\\/)?(?:m\\.|www\\.)?(?:youtu\\.be\\/|youtube\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))((\\w|-){11})(\\?\\S*)?'
        }

    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return

        for url in re.finditer(self.re['url'], message.content):
            await message.reply(url[0])


async def setup(bot):
    await bot.add_cog(YouTube(bot))
