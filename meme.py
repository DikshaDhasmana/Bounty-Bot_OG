import discord
from discord.ext import commands
import praw

reddit = praw.Reddit(
    client_id='IJEu0TUteYxIuR6NlkHoGg',
    client_secret='4B-p3g6CuipOeAVPEtedopQaRHkTKw',
    user_agent='LUFFY_BOT'
)

def setup(bot):
    @bot.command()
    async def meme(ctx):
        subreddit = reddit.subreddit('AnimeFunny') 
        meme_submission = subreddit.random()
        meme_url = meme_submission.url
        await ctx.send(meme_url)

    @bot.command()
    async def op_meme(ctx):
        subreddit = reddit.subreddit('MemePiece') 
        meme_submission = subreddit.random()
        meme_url = meme_submission.url
        await ctx.send(meme_url)
