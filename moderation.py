import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        
        embed = discord.Embed(title="Member Kicked", description=f"{member.display_name} has been kicked from the server.", color=discord.Color.red())
        await ctx.send(embed=embed)

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        
        embed = discord.Embed(title="Member Banned", description=f"{member.display_name} has been banned from the server.", color=discord.Color.dark_red())
        await ctx.send(embed=embed)

    @bot.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, id: int):
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        
        embed = discord.Embed(title="Member Unbanned", description="The user has been unbanned.", color=discord.Color.green())
        await ctx.send(embed=embed)
