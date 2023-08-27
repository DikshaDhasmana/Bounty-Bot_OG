import os
import io
import discord
import confess
import roast
import random
import meme
import datetime
import moderation
import sqlite3
import actions
import nakama
import poster
import help
import devilfruit
from keep_alive import keep_alive
from discord.ext import commands
from PIL import Image, ImageDraw, ImageOps

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

db_connection = sqlite3.connect('level_up_data.db')
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE IF NOT EXISTS users(guild_id INTEGER, user_id INTEGER, xp INTEGER, level INTEGER, role_id INTEGER, PRIMARY KEY (guild_id, user_id))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS nakamas(guild_id INTEGER, sender_id INTEGER, receiver_id INTEGER, PRIMARY KEY (guild_id, sender_id, receiver_id))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS treasure(user_id INTEGER PRIMARY KEY, berries INTEGER DEFAULT 0)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS daily_cooldown(user_id INTEGER PRIMARY KEY, last_usage TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS bounty (user_id INTEGER PRIMARY KEY, berry INTEGER)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS user_devil_fruits (user_id INTEGER PRIMARY KEY, devil_fruit TEXT)")

db_connection.commit()

def create_circular_thumbnail(image_path, border_color=(0, 0, 0), border_width=5):
    im = Image.open(image_path)
    im = im.convert("RGBA")
    
    # Calculate the dimensions for the larger canvas
    canvas_size = (im.width + 2 * border_width, im.height + 2 * border_width)
    
    # Create the larger canvas
    result = Image.new("RGBA", canvas_size)
    
    # Paste the circular image onto the larger canvas
    mask = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, im.size[0], im.size[1]), fill=255)
    
    # Calculate the position to paste the circular image with a border
    paste_position = (border_width, border_width)
    result.paste(im, paste_position, mask)
    
    # Draw the border around the circular image
    draw = ImageDraw.Draw(result)
    border_box = (
        border_width - 1, border_width - 1,
        result.width - border_width, result.height - border_width
    )
    draw.ellipse(border_box, outline=border_color, width=border_width)
    
    return result




@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    asyncio.create_task(clear_old_daily_cooldown_data())
    # Open the database connection here
    global db_connection
    db_connection = sqlite3.connect('level_up_data.db')
    global db_cursor
    db_cursor = db_connection.cursor()
  
  
@bot.event
async def on_member_join(member):
    server_name = member.guild.name
    print(f"Sending welcome message to {member.name}'s DM...")
    embed = discord.Embed(
        title = f"***Welcome {member.name}!***",
        description = f"\n𝑨𝒉𝒐𝒚, 𝒏𝒆𝒘 𝑵𝒂𝒌𝒂𝒎𝒂! 🏴‍☠️ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒂𝒃𝒐𝒂𝒓𝒅 𝒐𝒖𝒓 𝒍𝒆𝒈𝒆𝒏𝒅𝒂𝒓𝒚 𝒔𝒆𝒓𝒗𝒆𝒓, {𝒔𝒆𝒓𝒗𝒆𝒓_𝒏𝒂𝒎𝒆}! 𝑻𝒉𝒆 𝑮𝒓𝒂𝒏𝒅 𝑳𝒊𝒏𝒆 𝒂𝒘𝒂𝒊𝒕𝒔 𝒂𝒔 𝒚𝒐𝒖 𝒋𝒐𝒊𝒏 𝒐𝒖𝒓 𝒗𝒊𝒃𝒓𝒂𝒏𝒕 𝒄𝒓𝒆𝒘 𝒐𝒇 𝒇𝒂𝒏𝒔. 𝑭𝒓𝒐𝒎 𝒕𝒉𝒆 𝒎𝒚𝒔𝒕𝒊𝒄𝒂𝒍 𝑫𝒆𝒗𝒊𝒍 𝑭𝒓𝒖𝒊𝒕𝒔 𝒕𝒐 𝒆𝒑𝒊𝒄 𝒃𝒂𝒕𝒕𝒍𝒆𝒔 𝒂𝒏𝒅 𝒖𝒏𝒇𝒐𝒓𝒈𝒆𝒕𝒕𝒂𝒃𝒍𝒆 𝒄𝒉𝒂𝒓𝒂𝒄𝒕𝒆𝒓𝒔, 𝒘𝒆'𝒓𝒆 𝒉𝒆𝒓𝒆 𝒕𝒐 𝒔𝒉𝒂𝒓𝒆 𝒐𝒖𝒓 𝒍𝒐𝒗𝒆 𝒇𝒐𝒓 𝒕𝒉𝒊𝒔 𝒍𝒆𝒈𝒆𝒏𝒅𝒂𝒓𝒚 𝒘𝒐𝒓𝒍𝒅. 𝑺𝒆𝒕 𝒔𝒂𝒊𝒍 𝒘𝒊𝒕𝒉 𝒖𝒔 𝒂𝒏𝒅 𝒆𝒙𝒑𝒍𝒐𝒓𝒆 𝒕𝒉𝒆 𝒗𝒂𝒔𝒕 𝒔𝒆𝒂𝒔 𝒐𝒇 𝒅𝒊𝒔𝒄𝒖𝒔𝒔𝒊𝒐𝒏𝒔, 𝒕𝒉𝒆𝒐𝒓𝒊𝒆𝒔, 𝒂𝒏𝒅 𝒇𝒖𝒏 𝒂𝒄𝒕𝒊𝒗𝒊𝒕𝒊𝒆𝒔. 𝑾𝒉𝒆𝒕𝒉𝒆𝒓 𝒚𝒐𝒖'𝒓𝒆 𝒂 𝒔𝒆𝒂𝒔𝒐𝒏𝒆𝒅 𝒑𝒊𝒓𝒂𝒕𝒆 𝒐𝒓 𝒂 𝒓𝒐𝒐𝒌𝒊𝒆 𝒆𝒙𝒑𝒍𝒐𝒓𝒆𝒓, 𝒕𝒐𝒈𝒆𝒕𝒉𝒆𝒓, 𝒘𝒆'𝒍𝒍 𝒄𝒓𝒆𝒂𝒕𝒆 𝒎𝒆𝒎𝒐𝒓𝒊𝒆𝒔 𝒕𝒉𝒂𝒕 𝒓𝒊𝒗𝒂𝒍 𝒕𝒉𝒆 𝑺𝒕𝒓𝒂𝒘 𝑯𝒂𝒕 𝒄𝒓𝒆𝒘'𝒔 𝒐𝒘𝒏 𝒂𝒅𝒗𝒆𝒏𝒕𝒖𝒓𝒆𝒔. 𝑫𝒓𝒐𝒑 𝒂𝒏𝒄𝒉𝒐𝒓, 𝒓𝒆𝒍𝒂𝒙, 𝒂𝒏𝒅 𝒈𝒆𝒕 𝒓𝒆𝒂𝒅𝒚 𝒇𝒐𝒓 𝒂𝒏 𝒖𝒏𝒇𝒐𝒓𝒈𝒆𝒕𝒕𝒂𝒃𝒍𝒆 𝒋𝒐𝒖𝒓𝒏𝒆𝒚 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒕𝒉𝒆 𝒘𝒐𝒓𝒍𝒅 𝒐𝒇 𝑶𝒏𝒆 𝑷𝒊𝒆𝒄𝒆! ⚓🌊",
        color = 0x000000
    )
    if member.avatar:
        avatar_bytes = await member.avatar.read()
        avatar_io = io.BytesIO(avatar_bytes)
        circular_avatar = create_circular_thumbnail(avatar_io)
        circular_avatar_io = io.BytesIO()
        circular_avatar.save(circular_avatar_io, format="PNG")
        circular_avatar_io.seek(0)
        embed.set_thumbnail(url="attachment://circular_avatar.png")
    banner_path = os.path.join(os.path.dirname(__file__), "welcome.gif")
    embed.set_image(url="attachment://welcome.gif")
    try:
        await member.create_dm()
        await member.dm_channel.send(
            embed=embed,
            files=[
                discord.File(banner_path, "welcome.gif"),
                discord.File(circular_avatar_io, "circular_avatar.png")
            ]
        )
    except Exception as a:
        await print(f"An error occurred: {a}")




def calculate_level(xp):
    xp_required = 25 
    level = 0
    while xp >= xp_required:
        level += 1
        xp_required *= 2
    return level


def get_user_level(guild_id, user_id):
    db_cursor.execute("SELECT level FROM users WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    result = db_cursor.fetchone()
    if result:
        return result[0]
    return 0  # Default level if user is not found



def get_user_treasure(user_id):
    db_cursor.execute("SELECT berries FROM treasure WHERE user_id = ?", (user_id,))
    result = db_cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0  



def update_user_treasure(user_id, new_treasure):
    db_cursor.execute("INSERT OR REPLACE INTO treasure (user_id, berries) VALUES (?, ?)", (user_id, new_treasure))
    db_connection.commit()
  

@bot.event
async def on_message(message):
    if message.author.bot:
        return 
    user_id = message.author.id
    guild_id = message.guild.id  
    
    db_cursor.execute("INSERT OR IGNORE INTO users (guild_id, user_id, xp, level) VALUES (?, ?, ?, ?)", (guild_id, user_id, 0, 0))
    db_cursor.execute("UPDATE users SET xp = xp + 1 WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    db_connection.commit()
    db_cursor.execute("SELECT xp FROM users WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    xp = db_cursor.fetchone()[0]
    level = calculate_level(xp) 
    db_cursor.execute("SELECT xp, level FROM users WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    xp, old_level = db_cursor.fetchone()

    if level > old_level:
        reward = level * 1000 
        new_berry = reward + get_user_treasure(user_id) 
        new_bounty = level * 1000
        add_bounty(user_id, new_bounty)
        update_user_treasure(user_id, new_berry)

        berry_path = os.path.join(os.path.dirname(__file__), "berry.png")
        embed = discord.Embed(
            title=f"Congratulations, {message.author.display_name}!",
            description=f"You've leveled up to level {level}!\nYou've received <:image:1141659940109418557>{reward} as a level up reward!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url="attachment://berry.png")
        await message.channel.send(embed=embed, file=discord.File(berry_path,"berry.png"))
  
        db_cursor.execute("UPDATE users SET level = ? WHERE guild_id = ? AND user_id = ?", (level, guild_id, user_id))


    content = message.content.lower()
    if "meat" in content:
        responses = ["Hey, you said meat? Do you have any for me :star_struck: :star_struck: ?", "Meat!!! Where is meat?! Gimme all the meat out there :meat_on_bone: :meat_on_bone: !!"]
        response = random.choice(responses)
        await message.channel.send(response)
    await bot.process_commands(message)


@bot.command()
async def pro(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    user_id = member.id
    guild_id = ctx.guild.id  
    
    # Fetch user's XP, level, and devil fruit from the database
    db_cursor.execute("SELECT xp, level FROM users WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    result = db_cursor.fetchone()
    if result:
        xp, level = result
    else:
        xp, level = 0, 0
    
    db_cursor.execute("SELECT berry FROM bounty WHERE user_id = ?", (user_id,))
    bounty_result = db_cursor.fetchone()
    bounty = bounty_result[0] if bounty_result else 0
  
    user_treasure = get_user_treasure(user_id)
    
    # Fetch devil fruit information
    db_cursor.execute("SELECT devil_fruit FROM user_devil_fruits WHERE user_id = ?", (user_id,))
    devil_fruit_names = [row[0] for row in db_cursor.fetchall()]
    devil_fruit_text = "\n".join(devil_fruit_names) if devil_fruit_names else "No devil fruits"
    
    roles = ', '.join([role.name for role in member.roles])
    nakama_ids = get_nakama(guild_id, user_id)
    nakama_mentions = [ctx.guild.get_member(nakama_id[0]).mention for nakama_id in nakama_ids]
    nakama_text = "\n".join(nakama_mentions) if nakama_mentions else "None"
    
    embed = discord.Embed(
        title=f"{member.display_name}'s Profile",
        description=f"**XP:** {xp}\n**Level:** {level}\n**Treasure:** <:image:1141659940109418557>{user_treasure}\n**Bounty:** <:image:1141659940109418557>{bounty}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Nakama", value=nakama_text, inline=False)
    embed.add_field(name="Roles", value=roles, inline=False)
    embed.add_field(name="Joining Date", value=member.joined_at.strftime('%B %d, %Y'), inline=False)
    
    embed.add_field(name="Devil Fruits", value=devil_fruit_text, inline=False)
    
    if member.avatar:
        avatar_bytes = await member.avatar.read()
        avatar_io = io.BytesIO(avatar_bytes)
        circular_avatar = create_circular_thumbnail(avatar_io, border_color=(0, 0, 255), border_width=3)

        circular_avatar.save("circular_avatar.png")
        embed.set_thumbnail(url="attachment://circular_avatar.png")
    
    await ctx.send(embed=embed, file=discord.File("circular_avatar.png"))


def get_nakama(guild_id, user_id):
    db_cursor.execute("SELECT receiver_id FROM nakamas WHERE guild_id = ? AND sender_id = ?", (guild_id, user_id))
    return db_cursor.fetchall()


@bot.event
async def on_disconnect():
    pass


        
@bot.command()
async def sd(ctx, member: discord.Member, *, message: str):
    try:
        await member.create_dm()
        await member.dm_channel.send(message)
        await ctx.message.delete()
        await ctx.send(f"Message sent to {member.name}'s DM.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



@bot.command()
async def av(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    avatar_url = member.avatar.url
    if not avatar_url:
        await ctx.send("Avatar not found.")
    else:
        embed = discord.Embed(
            title=f"{member.display_name}'s Avatar",
            color=discord.Color.green()
        )
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)

@bot.command()
async def si(ctx):
    server = ctx.guild
    server_name = server.name
    date_created = server.created_at.strftime('%B %d, %Y')
    total_members = server.member_count
    human_members = sum(1 for member in server.members if not member.bot)
    bot_members = sum(1 for member in server.members if member.bot)
    admin_mentions = [admin.mention for admin in server.members if admin.guild_permissions.administrator]
    
    # Exclude @everyone and bot-managed roles
    role_mentions = [role.mention for role in server.roles if not role.is_bot_managed() and not role.is_default()]

    # Concatenate role mentions into a single string
    roles_text = ', '.join(role_mentions)

    embed = discord.Embed(title=f"{server_name}", color=discord.Color.og_blurple())

    if server.icon:
        icon_bytes = await server.icon.read()
        icon_io = io.BytesIO(icon_bytes)
        circular_icon = create_circular_thumbnail(icon_io, border_color=(0, 0, 255), border_width=3)

        circular_icon.save("circular_icon.png")
        embed.set_thumbnail(url="attachment://circular_icon.png")

    embed.add_field(name="Date of Formation", value=date_created, inline=False)
    embed.add_field(name="Total Members", value=total_members, inline=True)
    embed.add_field(name="Human Members", value=human_members, inline=True)
    embed.add_field(name="Bot Members", value=bot_members, inline=True)
    embed.add_field(name="Admins", value=', '.join(admin_mentions) if admin_mentions else 'No Admins', inline=False)

    # Split roles_text into multiple fields if its length exceeds 1024 characters
    while roles_text:
        embed.add_field(name="Roles", value=roles_text[:1024], inline=False)
        roles_text = roles_text[1024:]

    await ctx.send(embed=embed, file=discord.File("circular_icon.png"))







@bot.command()
async def lb(ctx):
    guild_id = ctx.guild.id
    db_cursor.execute("SELECT user_id, level FROM users WHERE guild_id = ? ORDER BY level DESC LIMIT 10", (guild_id,))
    top_users = db_cursor.fetchall()

    # Create an embed for the leaderboard
    embed = discord.Embed(
        title="Server Leaderboard",
        color=discord.Color.purple()
    )
    if top_users:
        for index, (user_id, level) in enumerate(top_users, start=1):
            user = ctx.guild.get_member(user_id)
            if user:
                embed.add_field(
                    name=f"{index}. {user.display_name}",
                    value=f"Level: {level}",
                    inline=False
                )
            else:
                embed.add_field(
                    name=f"{index}. User Not Found",
                    value=f"Level: {level}",
                    inline=False
                )
    else:
        embed.add_field(
            name="No Users Found",
            value="There are no users in the leaderboard.",
            inline=False
        )
    await ctx.send(embed=embed)




@bot.command()
async def rank(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    guild_id = ctx.guild.id
    user_id = member.id

    # Retrieve user's level and XP
    db_cursor.execute("SELECT level, xp FROM users WHERE guild_id = ? AND user_id = ?", (guild_id, user_id))
    result = db_cursor.fetchone()

    if result:
        level = result[0]
        xp = result[1]

        # Calculate user's rank
        db_cursor.execute("SELECT COUNT(*) FROM users WHERE guild_id = ? AND level > ? AND xp > ?", (guild_id, level, xp))
        user_rank = db_cursor.fetchone()[0] + 1

        # Create an embed for the rank information
        embed = discord.Embed(
            title=f"Rank for {member.display_name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Rank", value=f"{user_rank}", inline=True)
        embed.add_field(name="Level", value=f"{level}", inline=True)
        embed.add_field(name="XP", value=f"{xp}", inline=True)

        await ctx.send(embed=embed)
    else:
        await ctx.send("User information not found.")


import asyncio


@bot.command()
async def support(ctx):
    embed = discord.Embed(title="Support server", color=discord.Color.brand_green())
    embed.description = "For reporting any bugs or asking doubts regarding the bot, join https://discord.gg/WcUwsJsy and contact our bot support team."
    await ctx.send(embed=embed)


@bot.command()
async def daily(ctx):
    user_id = ctx.author.id
    guild_id = ctx.guild.id

    # Check if the user has already used the command within the last 24 hours
    current_time = datetime.datetime.now()
    last_usage_time_str = get_last_daily_usage(user_id)  # Replace with your function to get last daily usage timestamp
    
    if last_usage_time_str:
        # Parse the string into a datetime object, including fractional seconds
        last_usage_time = datetime.datetime.strptime(last_usage_time_str, '%Y-%m-%d %H:%M:%S.%f')  
        
        time_elapsed = current_time - last_usage_time
        time_remaining = datetime.timedelta(seconds=(24 * 60 * 60 - int(time_elapsed.total_seconds())))
        
        if time_elapsed.total_seconds() < 24 * 60 * 60:
            # Create a red embed with the already used message
            embed = discord.Embed(title="Daily Reward", color=discord.Color.red())
            embed.description = f"You've already claimed berries for today. Please wait {time_remaining} to redeem you daily rewards again."
            
            await ctx.send(embed=embed)
            return

    # Reward the user with berries based on their level
    user_treasure = get_user_treasure(user_id)
    level = get_user_level(guild_id, user_id)
    if level == 0:
      new_berry = 10
    else:
      new_berry = user_treasure + (level * 50)
    update_user_treasure(user_id, new_berry)

    # Update the last daily usage time in the database
    update_last_daily_usage(user_id, current_time)

    embed = discord.Embed(title="Daily Reward", color=0x00ff00)
    embed.add_field(name="User", value=ctx.author.mention, inline=False)
    if level == 0:
        embed.add_field(name="Reward", value="Received <:image:1141659940109418557>10 as daily reward.", inline=False)
    else:
      embed.add_field(name="Reward", value=f"Received  <:image:1141659940109418557>{level*50} as daily reward.", inline=False)
    embed.set_thumbnail(url="attachment://berry.png")
    await ctx.send(embed=embed, file=discord.File("berry.png"))



def get_last_daily_usage(user_id):
    db_cursor.execute("SELECT last_usage FROM daily_cooldown WHERE user_id = ?", (user_id,))
    result = db_cursor.fetchone()
    if result:
        return result[0]
    return None

def update_last_daily_usage(user_id, timestamp):
    db_cursor.execute("INSERT OR REPLACE INTO daily_cooldown (user_id, last_usage) VALUES (?, ?)", (user_id, timestamp))
    db_connection.commit()

def async_context(func):
    async def wrapper(*args, **kwargs):
        await asyncio.to_thread(lambda: func(*args, **kwargs))
    return wrapper

async def clear_old_daily_cooldown_data():
    await bot.wait_until_ready()
    while not bot.is_closed():
        db_cursor.execute("DELETE FROM daily_cooldown WHERE last_usage < ?", (datetime.datetime.now() - datetime.timedelta(days=1),))
        db_connection.commit()
        await asyncio.sleep(60 * 60)



def add_bounty(user_id, amount):
    db_cursor.execute("SELECT berry FROM bounty WHERE user_id = ?", (user_id,))
    result = db_cursor.fetchone()

    if result:
        current_bounty = result[0]
        new_bounty = current_bounty + amount

        db_cursor.execute("UPDATE bounty SET berry = ? WHERE user_id = ?", (new_bounty, user_id))
        db_connection.commit()
    else:
        db_cursor.execute("INSERT INTO bounty (user_id, berry) VALUES (?, ?)", (user_id, amount))
        db_connection.commit()



@bot.command()
async def blb(ctx):
    db_cursor.execute("SELECT user_id, berry FROM bounty ORDER BY berry DESC LIMIT 10")
    top_users = db_cursor.fetchall()

    # Create an embed for the leaderboard
    embed = discord.Embed(
        title="Global Bounty Leaderboard",
        color=discord.Color.gold()
    )
    
    if top_users:
        for index, (user_id, berry) in enumerate(top_users, start=1):
            # Fetch user information using the User endpoint
            user = await bot.fetch_user(user_id)
            if user:
                embed.add_field(
                    name=f"{index}. {user.name}",
                    value=f"Bounty: <:image:1141659940109418557>{berry}",
                    inline=False
                )
            else:
                embed.add_field(
                    name=f"{index}. User ID: {user_id}",
                    value=f"Bounty: <:image:1141659940109418557>{berry}",
                    inline=False
                )
    else:
        embed.add_field(
            name="No Users Found",
            value="There are no users in the leaderboard.",
            inline=False
        )
    await ctx.send(embed=embed)

@bot.command()
async def br(ctx):
    # Get the user's ID
    user_id = ctx.author.id
    
    # Query the database to find the user's rank
    db_cursor.execute("SELECT COUNT(*) FROM bounty WHERE berry > (SELECT berry FROM bounty WHERE user_id = ?)", (user_id,))
    user_rank = db_cursor.fetchone()[0] + 1

    # Get the user's bounty
    db_cursor.execute("SELECT berry FROM bounty WHERE user_id = ?", (user_id,))
    user_bounty = db_cursor.fetchone()

    if user_bounty:
        user_bounty = user_bounty[0]

    # Send a message with the user's global rank and bounty
    await ctx.send(f"Your Global Rank: {user_rank}\nYour Bounty: <:image:1141659940109418557>{user_bounty}")



moderation.setup(bot)
confess.setup(bot)
roast.setup(bot)
meme.setup(bot)
actions.setup(bot)
nakama.setup(bot)
poster.setup(bot)
help.setup(bot)
devilfruit.setup(bot)

import configparser

config = configparser.ConfigParser()
config.read('config.ini')  # Use the appropriate file name

bot_token = config['credentials']['bot_token']

bot.run(bot_token)
keep_alive()