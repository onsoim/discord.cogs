
from discord                import File
from discord.ext.commands   import Cog
from pytube                 import YouTube  as YT

import os
import re


class YouTube(Cog):
    def __init__(self, bot):
        # print('init youtube cog')
        self.bot    = bot
        self.re     = {
            'url': r'((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?'
        }
        self.data   = './data'
        os.makedirs(self.data, exist_ok=True)

    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return

        for url in re.finditer(self.re['url'], message.content):
            yt = YT(url[0])

            filename = f'{self.data}/{yt.video_id}.mp4'
            yt.streams.get_highest_resolution().download(self.data, f'{yt.video_id}.mp4')

            # await message.reply(yt.video_id if os.path.getsize(filename) < 8388608 else "File size exceeds 8MB.")
            if os.path.getsize(filename) < 8388608:
                await message.channel.send(
                    yt.title,
                    file = File(filename),
                    reference = message
                )


async def setup(bot):
    await bot.add_cog(YouTube(bot))
