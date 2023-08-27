import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def hug(ctx, target: discord.Member):
        gif_url = "https://i.pinimg.com/originals/b8/7f/8b/b87f8b1e2732c534a00937ffb24baa79.gif"  
        embed = discord.Embed(title=f"{ctx.author.display_name} hugs {target.display_name} tight!", color=discord.Color.blue())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def smooch(ctx, target: discord.Member):
        gif_url = "https://31.media.tumblr.com/28fd3feae07b8f32355bad331d0ef6c7/tumblr_mhet2eDOOV1rec05yo1_500.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} gives {target.display_name} an intense smooch!", color=discord.Color.dark_magenta())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def highfive(ctx, target: discord.Member):
        gif_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzN2MWVjdW43cmIxaXNuYjNzdHdtOG5oaTZpNnI3NTBkdjFwcWl4dyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/10LKovKon8DENq/giphy.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} gives {target.display_name} a HighFive!", color=discord.Color.green())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def clap(ctx):
        gif_url = "https://i.gifer.com/JEVP.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} applauds!", color=discord.Color.orange())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def kiss(ctx, target: discord.Member):
        gif_url = "https://media.tenor.com/4Z5a0xqgXAUAAAAC/anime-kiss.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} gives {target.display_name} a sweet kiss!", color=discord.Color.magenta())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def slap(ctx, target: discord.Member):
        gif_url = "https://gifdb.com/images/high/mad-gangster-anime-slap-nnulodryf9gpmj9n.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} slaps {target.display_name} hard!", color=discord.Color.yellow())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def kill(ctx, target: discord.Member):
        gif_url = "https://i.makeagif.com/media/5-02-2015/4zufR6.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} kills {target.display_name} brutally!", color=discord.Color.dark_red())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def punch(ctx, target: discord.Member):
        gif_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDY4NzZmNW1lYjk0bzZ5NDE5ZDg2ODhxaXV6aTZ0c25tNXl1ZjBmZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/arbHBoiUWUgmc/giphy.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} gives {target.display_name} a power punch!", color=discord.Color.dark_red())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)


    @bot.command()
    async def happy(ctx):
        gif_url = "https://media.tenor.com/EbNeN8Sf8QwAAAAM/umaru-hyper.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} is extremely happy!", color=discord.Color.blurple())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def sad(ctx):
        gif_url = "https://gifdb.com/images/high/sad-anime-umau-doma-ot386njcsketfjqv.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} is extremely sad!", color=discord.Color.light_gray())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def mock(ctx, target: discord.Member):
        gif_url = "https://media.tenor.com/_4G3kqs1rPEAAAAC/anime-laugh-anime-smile.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} makes fun of {target.display_name}!", color=discord.Color.dark_teal())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

    @bot.command()
    async def laugh(ctx):
        gif_url = "https://i.pinimg.com/originals/4d/f1/8e/4df18e92e572823631919cf33de69900.gif" 
        embed = discord.Embed(title=f"{ctx.author.display_name} finds it funny!", color=discord.Color.brand_green())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)


