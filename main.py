import os
import youtube_dl
from discord.ext import commands
from src.Music import Music
from dotenv import load_dotenv, find_dotenv


# dotenv setup
load_dotenv(find_dotenv())

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


bot = commands.Bot('1', description='Yet another music bot.')
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
    print('{0.user.name} - Started'.format(bot))

bot.run(os.environ.get("TOKEN"))
