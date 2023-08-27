import discord
from discord.ext import commands

def setup(bot):
  @bot.command(name='com')
  async def custom_help(ctx):
    embed = discord.Embed(
      title="Command List",
      description="Here are the available commands and their descriptions:",
      color=discord.Color.blue()
    )
    
    # Add command descriptions
    embed.add_field(name="Utility Commands", value="\n**.daily :**  Claim your daily rewards.\n**.pro or .pro @ :**  View your/someone's server profile.\n**.si :**  View server information.\n**.lb :**  View server leaderboard.\n**.rank or .rank @ :**  View your/someone's server rank.\n**.bounty or .bounty @ :**  View your/someone's Bounty Poster.\n**.av or .av @ :**  View your/someone's avatar.\n**.com :**  View this message.\n", inline=False)
    embed.add_field(name="Nakama Commands", value="\n**.an @ :**  Add someone to your Nakama list.\n**.ra @ :**  Remove someone from your Nakama list.\n**.db @ <amount> :**  Donate Berry to any of your Nakama.\n", inline=False)
    embed.add_field(name="Fun Commands", value="\n**.confess <text> :**  Create an anonymous confession.\n**.meme :**  Get an Anime meme.\n**.op_meme :**  Get an One Piece meme.\n**.roast @ :**  Roast someone. (Note: Might be offensive).\n**.roast_hindi @ :**  Roast someone in Hindi. (Note: Might be abusive.)\n**.sd @ :**  Send anonymous DM to someone. (Note: Kindly report to the server if recieved any unwanted offensive DM.)\n", inline=False)
    embed.add_field(name="Action Commands", value="\n**.hug @ :**  Hug someone.\n**.kiss @ :**""  Kiss someone.\n**.smooch @ :**  Give a smooch to someone.\n**.slap @ :**  Slap someone.\n**.punch @ :**  Punch someone.\n**.kill @ :**  Kill someone.\n**.mock @ :**  Make fun of someone.\n**.laugh :**  Laugh.\n**.sad :**  Show sad emotion.\n**.happy :**  Show happy emotion.\n", inline=False)
    embed.add_field(name="Moderation Commands", value="\n**.kick @ :**  Kick someone from server.\n**.ban @ :**  Ban server from server.\n**.unban <id> :**  Unban someone from server.\n", inline=False)
    embed.add_field(name="AI Chat Commands", value="\n**/beginstorymode :**  Chatbot will respond to your message when @mentioned.\n**/endstorymode :**  Chatbot will stop responding to pings.", inline=False)
    embed.add_field(name=".support", value="Join OG server to get bot support.", inline=False)
    # Add more command descriptions here
    
    await ctx.send(embed=embed)