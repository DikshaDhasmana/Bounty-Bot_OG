import discord
from discord.ext import commands
import sqlite3
import asyncio

db_connection = sqlite3.connect("level_up_data.db")
db_cursor = db_connection.cursor()

def setup(bot):
    @bot.command(name="an")
    async def add_nakama(ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send("You cannot add yourself as your own Nakama!")
            return

        confirmation_embed = discord.Embed(
            title=f"Add {ctx.author.display_name} as your Nakama?",
            description=f"{member.mention}, do you accept the invitation? Type 'y' or 'Y' to accept, or wait for the timeout.",
            color=discord.Color.blue()
        )

        confirmation_message = await ctx.send(embed=confirmation_embed)

        def check(response):
            return response.author == member and response.content.lower() in ["y", "yes", "n", "no"]

        try:
            response = await bot.wait_for("message", check=check, timeout=30)  # Increased timeout to 30 seconds
        except asyncio.TimeoutError:
            await confirmation_message.edit(embed=discord.Embed(title="Invitation Expired", description="The invitation has expired. Please respond within 30 seconds next time.", color=discord.Color.red()))
        else:
            if response.content.lower() in ["y", "yes"]:
                await confirmation_message.edit(embed=discord.Embed(title="Invitation Accepted", color=discord.Color.green()))

                # Add the member to the Nakama list in the database
                add_nakama_relationship(ctx.guild.id, ctx.author.id, member.id)

                # Notify both users about becoming Nakama
                await ctx.send(f"{member.display_name} and {ctx.author.display_name} are now Nakama!")
            elif response.content.lower() in ["n", "no"]:
                await confirmation_message.edit(embed=discord.Embed(title="Invitation Declined", color=discord.Color.red()))

    @bot.command(name="rn")
    async def remove_nakama(ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send("You cannot remove yourself from your own Nakama!")
            return

        confirmation_embed = discord.Embed(
            title=f"Remove {member.display_name} as your Nakama?",
            description=f"{ctx.author.mention}, are you sure you want to remove {member.display_name} as your Nakama? Type 'y' or 'Y' to confirm, or wait for the timeout.",
            color=discord.Color.blue()
        )

        confirmation_message = await ctx.send(embed=confirmation_embed)

        def check(response):
            return response.author == ctx.author and response.content.lower() in ["y", "yes", "n", "no"]

        try:
            response = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await confirmation_message.edit(embed=discord.Embed(title="Confirmation Expired", description="The confirmation has expired. Please respond within 30 seconds next time.", color=discord.Color.red()))
        else:
            if response.content.lower() in ["y", "yes"]:
                await confirmation_message.edit(embed=discord.Embed(title="Confirmation Accepted", color=discord.Color.green()))

                # Remove the Nakama relationship from the database
                remove_nakama_relationship(ctx.guild.id, ctx.author.id, member.id)

                # Notify both users about Nakama removal
                await ctx.send(f"{member.display_name} and {ctx.author.display_name} are no longer Nakama.")
            elif response.content.lower() in ["n", "no"]:
                await confirmation_message.edit(embed=discord.Embed(title="Confirmation Declined", color=discord.Color.red()))

    @bot.command(name="db")
    async def donate_berry(ctx, receiver: discord.Member, amount: int):
        sender_id = ctx.author.id
        guild_id = ctx.author.guild.id

        # Check if sender and receiver are Nakama
        if are_nakama(guild_id, sender_id, receiver.id):
            # Deduct berries from the sender
            if deduct_berries(sender_id, amount):
                # Add berries to the receiver
                add_berries(receiver.id, amount)

                # Create and send an embed message
                embed = discord.Embed(
                    title="Berry Donation",
                    description=f"You've donated <:image:1141659940109418557>{amount} to {receiver.display_name}!",
                    color=discord.Color.green()
                )
                embed.set_thumbnail(url="attachment://berry.png")
                await ctx.send(embed=embed, file=discord.File("berry.png")) 
            else:
                # Create and send an error embed message
                embed = discord.Embed(
                    title="Error",
                    description="You don't have enough berries to donate.",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
        else:
            # Create and send an error embed message
            embed = discord.Embed(
                title="Error",
                description="You can only donate berries to your Nakama.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def are_nakama(guild_id, user1_id, user2_id):
    db_cursor.execute("SELECT * FROM nakamas WHERE guild_id = ? AND ((sender_id = ? AND receiver_id = ?) OR (sender_id = ? AND receiver_id = ?))", (guild_id, user1_id, user2_id, user2_id, user1_id))
    return db_cursor.fetchone() is not None


def deduct_berries(user_id, amount):
    db_cursor.execute("SELECT berries FROM treasure WHERE user_id = ?", (user_id,))
    result = db_cursor.fetchone()

    if result and result[0] >= amount:
        db_cursor.execute("UPDATE treasure SET berries = berries - ? WHERE user_id = ?", (amount, user_id))
        db_connection.commit()
        return True

    return False

# Function to add berries to the receiver
def add_berries(user_id, amount):
    db_cursor.execute("UPDATE treasure SET berries = berries + ? WHERE user_id = ?", (amount, user_id))
    db_connection.commit()

# Function to add Nakama relationship to the database
def add_nakama_relationship(guild_id, sender_id, receiver_id):
    db_cursor.execute("INSERT INTO nakamas (guild_id, sender_id, receiver_id) VALUES (?, ?, ?)", (guild_id, sender_id, receiver_id))
    db_cursor.execute("INSERT INTO nakamas (guild_id, sender_id, receiver_id) VALUES (?, ?, ?)", (guild_id, receiver_id, sender_id))  # Add the reverse relationship
    db_connection.commit()

# Function to remove Nakama relationship from the database
def remove_nakama_relationship(guild_id, sender_id, receiver_id):
    db_cursor.execute("DELETE FROM nakamas WHERE guild_id = ? AND sender_id = ? AND receiver_id = ?", (guild_id, sender_id, receiver_id))
    db_cursor.execute("DELETE FROM nakamas WHERE guild_id = ? AND sender_id = ? AND receiver_id = ?", (guild_id, receiver_id, sender_id))  # Remove the reverse relationship
    db_connection.commit()
