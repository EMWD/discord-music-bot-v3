import os
import youtube_dl
from discord.ext import commands
from src.Common import Common
from src.Music import Music
from helpers.dotenv_setup import env


# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


bot = commands.Bot('!', description='Kusic the music bot.')
bot.add_cog(Music(bot))
bot.add_cog(Common(bot))


@bot.event
async def on_ready():
    print('{0.user.name} - Started'.format(bot))

bot.run(env.get("TOKEN"))
