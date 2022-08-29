import nextcord
from nextcord.ext import commands
from Natty.config import VERSION


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        
    @commands.command(brief="Gets the latency to Discords API")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f":ping_pong: Pong! **{ctx.bot.latency * 1000:.2f}ms**")
        
    @commands.command(brief="Displays information about the bot")
    async def about(self, ctx: commands.Context):
        embed = nextcord.Embed(
            title="About Natty",
            description="TBD",
            color=nextcord.Color.blue()
        )
        embed.set_thumbnail(self.bot.user.avatar.url)
        embed.set_footer(text=f"{self.bot.user.name} · version {VERSION}")
        
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Main(bot))
