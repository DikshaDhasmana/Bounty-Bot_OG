import discord
from discord.ext import commands
import requests
import random

def setup(bot):
    @bot.command()
    async def roast(ctx, member: discord.Member):
        if member == bot.user:
            await ctx.send("I'm too awesome for roasts!")
        else:
            response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
            if response.status_code == 200:
                insult = response.json()["insult"]
                await ctx.send(f"{member.mention}, {insult}")
            else:
                await ctx.send("Oops! Something went wrong while fetching a roast.")

    @bot.command()
    async def roast_hindi(ctx, member: discord.Member):
        if member == bot.user:
            await ctx.send("Pehli fursat me nikal!")
        
        else:
            response = requests.get("https://evilinsult.com/generate_insult.php?lang=hi&type=json")
            if response.status_code == 200:
                insult = response.json()["insult"]
                await ctx.send(f"{member.mention}, {insult}")
            else:
                await ctx.send("Oops! Something went wrong while fetching a roast.")
