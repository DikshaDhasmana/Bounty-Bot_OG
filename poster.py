from PIL import Image, ImageDraw, ImageFont
import discord
import sqlite3
import os
import requests
from io import BytesIO
from discord.ext import commands

db_connection = sqlite3.connect("level_up_data.db")
db_cursor = db_connection.cursor()

def setup(bot):
    @bot.command(name="bounty")
    async def generate_bounty_poster(ctx, member: discord.Member = None):
        try:
            # Load the template image
            template_path = "background.png"
            poster = Image.open(template_path)

            if member is None:
                member = ctx.author

            user_id = member.id
            user_name = member.name

            db_cursor.execute("SELECT berry FROM bounty WHERE user_id = ?", (user_id,))
            bounty_result = db_cursor.fetchone()
            bounty = bounty_result[0] if bounty_result else 0

            # Define text and font settings
            font_filename = "Times New Roman MT Extra Bold.ttf"  # Replace with the actual font filename
            font_path = os.path.join(os.path.dirname(__file__), font_filename)
            name_font_size = 70
            bounty_font_size = 45
            name_font = ImageFont.truetype(font_path, size=name_font_size)
            bounty_font = ImageFont.truetype(font_path, size=bounty_font_size)
            draw = ImageDraw.Draw(poster)

            # Configure text color using provided RGB values
            text_color = (78, 44, 42)

            # Define text positions based on the template
            name_box = draw.textbbox((0, 0), user_name, font=name_font)
            name_width = name_box[2] - name_box[0]
            name_position = ((poster.width - name_width) // 2, 825)

            bounty_position = (150, 970)

            # Fetch and paste the member's avatar
            avatar_url = member.avatar.url
            response = requests.get(avatar_url)
            avatar_image = Image.open(BytesIO(response.content))
            avatar_image = avatar_image.resize((633, 483))  # Resize the avatar to fit

            # Paste the template image
            poster.paste(avatar_image, (63, 248))

            # Draw user name and bounty on the poster
            draw.text(name_position, user_name, font=name_font, fill=text_color)
            draw.text(bounty_position, f"{bounty}", font=bounty_font, fill=text_color)

            # Save the generated poster
            poster.save("bounty_poster.png")
            poster_file = discord.File("bounty_poster.png")
            embed = discord.Embed(title="Bounty Poster", description=f"Bounty poster for {user_name}")
            embed.set_image(url="attachment://bounty_poster.png")
            await ctx.send(embed=embed, file=poster_file)
            print("Bounty poster generated successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
