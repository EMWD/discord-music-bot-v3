import asyncio
from icecream import ic
from discord.ext import commands
from helpers.dotenv_setup import env


class Common(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    async def clean(self, ctx: commands.Context, lines_amount=2, delay=1):
        '''Delete certain amount of messages in text channel with some delay'''
        await asyncio.sleep(delay)
        await ctx.channel.purge(limit=lines_amount)

    @commands.command(name='i', aliases=['iam', 'who'])
    @commands.has_permissions(manage_guild=True)
    async def _iam(self, ctx: commands.Context):
        """Shows info about bot."""
        await ctx.send('My name is: {0.user.name}\nId is: {0.user.id}'.format(self.bot))
        await self.clean(ctx=ctx)

    @commands.command(name='answer', aliases=['an'])
    async def _answer(self, ctx: commands.Context):
        await ctx.send('Some text for answer')

    @commands.command(name='ping')
    async def _ping(self, ctx: commands.Context):
        await ctx.send('pong')

    if env.get("DEBUG") == 'True':
        @commands.command(name='text_full_wipe', aliases=['tfw'])
        async def _text_full_wipe(self, ctx: commands.Context):
            """Useful function for text channel cleaning. DONT USE THIS IN PROD"""
            await self.clean(ctx=ctx, lines_amount=None, delay=0)
