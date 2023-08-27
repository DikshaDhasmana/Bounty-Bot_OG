import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def confess(ctx, *, confession_text):
        embed = discord.Embed(description=confession_text, color=discord.Color.pink())
        embed.set_footer(text="Anonymous Confession")
        await ctx.send(embed=embed)
        await ctx.message.delete() 
