import discord
import sqlite3
from discord.ext import commands
import random

db_connection = sqlite3.connect("level_up_data.db")
db_cursor = db_connection.cursor()

devil_fruits = [
    {
      # L O G I A   D E V I L   F R U I T S
      
        "Eng_name": "Dark-Dark Fruit",
        "name": "Yami Yami no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control darkness, as well as transform into that element.",
        "damage_multiplier": 3.0,
        "life_booster": 1.8,
        "lucky_charm": 1.8,
        "acquisition": "Shop",
        "price": 2000000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/f/f5/Yami_Yami_no_Mi_Infobox.png/revision/latest?cb=20160123174331"
    },
    {
        "Eng_name": "Mag-Mag Fruit",
        "name": "Magu Magu no Mi",
        "type": "Logia",
        "ability": "Hailed as the Devil Fruit with the greatest attacking power, it allows users to create and control magma, as well as transform into that element.",
        "damage_multiplier": 2.8,
        "life_booster": 1.7,
        "lucky_charm": 1.7,
        "acquisition": "Shop",
        "price": 1700000,
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/a/ad/Magu_Magu_no_Mi.png/revision/latest?cb=20201109055107"
    },
    {
        "Eng_name": "Glint-Glint Fruit",
        "name": "Pika Pika no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control light, as well as transform into that element.",
        "damage_multiplier": 2.6,
        "life_booster": 1.6,
        "lucky_charm": 1.6,
        "acquisition": "Shop",
        "price": 1400000,
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/7/7f/PikaPikaYuh.png/revision/latest?cb=20201109133239"
    },
    {
        "Eng_name": "Rumble-Rumble Fruit",
        "name": "Goro Goro no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control lightning, as well as transform into that element.",
        "damage_multiplier": 2.4,
        "life_booster": 1.5,
        "lucky_charm": 1.5,
        "acquisition": "Shop",
        "price": 1100000,
        "image_url": "https://static.wikia.nocookie.net/grand-piece-online/images/8/86/Newgoro.png/revision/latest?cb=20220624192601"
    },
    {
        "Eng_name": "Ice-Ice Fruit",
        "name": "Hie Hie no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control ice, as well as transform into that element.",
        "damage_multiplier": 2.2,
        "life_booster": 1.4,
        "lucky_charm": 1.4,
        "acquisition": "Shop",
        "price": 800000,
        "image_url": "https://static.wikia.nocookie.net/onepiecefanon/images/1/13/Hie_Hie_no_Mi.png/revision/latest?cb=20211010181647"
    },
    {
        "Eng_name": "Flame-Flame Fruit",
        "name": "Mera Mera no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control fire, as well as transform into that element.",
        "damage_multiplier": 2.0,
        "life_booster": 1.3,
        "lucky_charm": 1.3,
        "acquisition": "Shop",
        "price": 500000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/8/8c/Mera_Mera_no_Mi_Infobox.png/revision/latest?cb=20151123200729"
    },
    {
        "Eng_name": "Sand-Sand Fruit",
        "name": "Suna Suna no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control sand, as well as transform into that element.",
        "damage_multiplier": 1.8,
        "life_booster": 1.8,
        "acquisition": "Shop",
        "price": 200000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/7/7d/Suna_Suna_no_Mi_Infobox.png/revision/latest?cb=20220408131752"
    },
    {
        "Eng_name": "Gas-Gas Fruit",
        "name": "Gasu Gasu no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control gas, as well as transform into that element.",
        "damage_multiplier": 1.6,
        "life_booster": 1.6,
        "acquisition": "Shop",
        "price": 140000,
        "image_url": "https://pm1.aminoapps.com/7463/460c71d92172a4d0813575db4c603a7575fb39c3r1-470-531v2_uhq.jpg"
    },
    {
        "Eng_name": "Snow-Snow Fruit",
        "name": "Yuki Yuki no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control snow, as well as transform into that element.",
        "damage_multiplier": 1.4,
        "life_booster": 1.4,
        "acquisition": "Shop",
        "price": 80000,
        "image_url": "https://static.wikia.nocookie.net/grand-piece-online/images/d/d3/Yuki.png/revision/latest?cb=20221227130525"
    },
    {
        "Eng_name": "Smoke-Smoke Fruit",
        "name": "Moku Moku no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control smoke, as well as transform into that element.",
        "damage_multiplier": 1.2,
        "life_booster": 1.2,
        "acquisition": "Shop",
        "price": 20000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/8/8d/Moku_Moku_no_Mi_Infobox.png/revision/latest?cb=20200912191830"
    },
    {
        "Eng_name": "Swamp-Swamp Fruit",
        "name": "Numa Numa no Mi",
        "type": "Logia",
        "ability": "Allows users to create and control mud, as well as transform into that element.",
        "damage_multiplier": 1.1,
        "life_booster": 1.1,
        "acquisition": "Shop",
        "price": 14000,
        "image_url": "https://img.elo7.com.br/product/original/465F7B6/action-figure-akuma-no-mi-numa-numa-no-mi-one-piece.jpg"
    },


  
  # P A R A M E C I A   F R U I T S
    {
        "Eng_name": "Tremor-Tremor Fruit",
        "name": "Gura Gura no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create destructive shockwaves and reshape landscapes.",
        "damage_multiplier": 4.0,
        "life_booster": 1.8,
        "lucky_charm": 1.8,
        "acquisition": "Shop",
        "price": 3000000,  # High power warrants a higher price
        "image_url": "https://preview.redd.it/nd7yujwe5ss81.png?width=600&format=png&auto=webp&s=897685d5f796b9a7f116e25fc42a02666567ed6d"
    },
    {
        "Eng_name": "Op-Op Fruit",
        "name": "Ope Ope no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create a spherical territory for various surgical operations.",
        "damage_multiplier": 3.8,
        "life_booster": 1.7,
        "lucky_charm": 1.7,
        "acquisition": "Shop",
        "price": 2700000,  # Unique abilities but not overwhelmingly destructive
        "image_url": "https://preview.redd.it/if-laws-fruit-in-one-pieace-is-called-ope-ope-no-mi-might-v0-nzl5wuxfcf1a1.png?width=640&crop=smart&auto=webp&s=cf1a682040c8c28875114f378a390a5caa23bc4c"
    },
    {
        "Eng_name": "Soul-Soul Fruit",
        "name": "Soru Soru no Mi",
        "type": "Paramecia",
        "ability": "Allows users to manipulate souls and control homies.",
        "damage_multiplier": 3.6,
        "life_booster": 1.6,
        "lucky_charm": 1.6,
        "acquisition": "Shop",
        "price": 2400000,  # Unique abilities with moderate offensive potential
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/5/59/Soru_-_Infobox.png/revision/latest?cb=20200203014158"
    },
    {
        "Eng_name": "Love-Love Fruit",
        "name": "Mero Mero no Mi",
        "type": "Paramecia",
        "ability": "Allows users to turn people to stone by making them fall in love.",
        "damage_multiplier": 3.4, 
        "life_booster": 1.5,
        "lucky_charm": 1.5,
        "acquisition": "Shop",
        "price": 2100000,  # Limited combat use, priced lower
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/9/98/Mero_Mero_no_Mi_Infobox.png/revision/latest?cb=20230306202058"
    },
    {
        "Eng_name": "Gravity-Gravity Fruit",
        "name": "Zushi Zushi no Mi",
        "type": "Paramecia",
        "ability": "Allows users to control gravity and manipulate its effects.",
        "damage_multiplier": 3.2,
        "life_booster": 1.4,
        "lucky_charm": 1.4,
        "acquisition": "Shop",
        "price": 1800000,  # Powerful manipulation of gravity justifies a higher price
        "image_url": "https://static.wikia.nocookie.net/grand-piece-online/images/9/9a/Zushi-new-fruit-pngpng.png/revision/latest?cb=20230129125200"
    },
    {
        "Eng_name": "Float-Float Fruit",
        "name": "Fuwa Fuwa no Mi",
        "type": "Paramecia",
        "ability": "Allows users to levitate and control the weight of objects.",
        "damage_multiplier": 3.0,
        "life_booster": 1.8,
        "acquisition": "Shop",
        "price": 1500000,
        "image_url": "https://static.wikia.nocookie.net/roblox-opl/images/c/c8/Float.png/revision/latest?cb=20180927033358"
    },
    {
        "Eng_name": "Hobby-Hobby Fruit",
        "name": "Hobi Hobi no Mi",
        "type": "Paramecia",
        "ability": "Allows users to turn living beings into toys and manipulate their memories.",
        "damage_multiplier": 2.8,
        "life_booster": 1.7,
        "acquisition": "Shop",
        "price": 1200000,  # Unique mind-manipulation abilities warrant a higher price
        "image_url": "https://static.wikia.nocookie.net/onepiecefanon/images/3/3b/Hobi_Hobi_no_Mi.png/revision/latest?cb=20220903093532"
    },
    {
        "Eng_name": "Paw-Paw Fruit",
        "name": "Nikyu Nikyu no Mi",
        "type": "Paramecia",
        "ability": "Allows users to repel anything they touch.",
        "damage_multiplier": 2.6,
        "life_booster": 1.6,
        "acquisition": "Shop",
        "price": 800000,
        "image_url": "https://static.wikia.nocookie.net/onepiecefanon/images/b/be/Nikyu_Nikyu_no_Mi._Infobox.png/revision/latest?cb=20220316155448"
    },
    {
        "Eng_name": "Venom-Venom Fruit",
        "name": "Doku Doku no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create and control poison, as well as transform into that element.",
        "damage_multiplier": 2.4,
        "life_booster": 1.5,
        "acquisition": "Shop",
        "price": 500000,  # Powerful poison manipulation justifies a higher price
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/d/dc/Doku_Doku_no_Mi.png/revision/latest/scale-to-width/360?cb=20201128172756"
    },
    {
        "Eng_name": "Brain-Brain Fruit",
        "name": "Nomi Nomi no Mi",
        "type": "Paramecia",
        "ability": "Allows users to turn objects and people into fruit, absorbing their traits.",
        "damage_multiplier": 2.2,
        "life_booster": 1.4,
        "acquisition": "Shop",
        "price": 200000,
        "image_url": "https://pic-bstarstatic.akamaized.net/ugc/03aac3a9cd5f6557787cc66de72218ad.jpg"
    },
    {
        "Eng_name": "Mochi-Mochi Fruit",
        "name": "Mochi Mochi no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create and control mochi, a sticky rice cake substance.",
        "damage_multiplier": 2.0,
        "life_booster": 1.3,
        "acquisition": "Shop",
        "price": 140000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/2/2c/Mochi_Mochi_no_Mi_Infobox.png/revision/latest?cb=20220525022420"
    },
    {
        "Eng_name": "String-String Fruit",
        "name": "Ito Ito no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create and control strings, granting versatile manipulation.",
        "damage_multiplier": 1.8,
        "acquisition": "Shop",
        "price": 80000,  # Wide range of applications justifies a higher price
        "image_url": "https://i.pinimg.com/736x/98/3c/f9/983cf9195e434436ec62438ee0a3cd7c.jpg"
    },
    {
        "Eng_name": "Barrier-Barrier Fruit",
        "name": "Bari Bari no Mi",
        "type": "Paramecia",
        "ability": "Allows users to create barriers/shields at will.",
        "damage_multiplier": 1.6,
        "acquisition": "Shop",
        "price": 20000,
        "image_url": "https://staticg.sportskeeda.com/editor/2022/10/47e60-16661871839293.png"
    },
    {
        "Eng_name": "Flower-Flower Fruit",
        "name": "Hana Hana no Mi",
        "type": "Paramecia",
        "ability": "Allows users to sprout additional limbs from any surface.",
        "damage_multiplier": 1.4,
        "acquisition": "Shop",
        "price": 17000,
        "image_url": "https://ih1.redbubble.net/image.2409304986.0146/st,small,507x507-pad,600x600,f8f8f8.jpg"
    },
    {
        "Eng_name": "Slow-Slow Fruit",
        "name": "Noro Noro no Mi",
        "type": "Paramecia",
        "ability": "Allows users to emit light that slows down whatever it touches.",
        "damage_multiplier": 1.2,
        "acquisition": "Shop",
        "price": 14000,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-JEbcwlEDnZke2jc2fk4Pl1pm3VhVXk-vF_wpDvVLAls9iZzrdu68oEaw87M6VzlojWc&usqp=CAU"
    },
    {
        "Eng_name": "Time-Time Fruit",
        "name": "Toki Toki no Mi",
        "type": "Paramecia",
        "ability": "Allows users to travel through time, but only to the future.",
        "damage_multiplier": 1.1,
        "acquisition": "Shop",
        "price": 11000,
        "image_url": "https://i.pinimg.com/originals/f7/c8/45/f7c84521e1223dbaa34443bb61496323.png"
    },
    {

      # M Y T H I C A L   Z O A N   F R U I T S
        "Eng_name": "Human-Human Fruit, Model: Buddha",
        "name": "Hito Hito no Mi, Model: Nika",
        "type": "Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a golden Buddha statue.",
        "damage_multiplier": 5.0,
        "life_booster": 1.8,
        "lucky_charm": 1.8,
        "acquisition": "Shop",
        "price": 4000000,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpcx-t268T9ieG4TKzd6p2nMoGwc3OTm6WIw&usqp=CAU"
    },
    {
        "Eng_name": "Fish-Fish Fruit, Model: Azure Dragon",
        "name": "Uo Uo no Mi, Model: Seiryu",
        "type": "Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a blue dragon.",
        "damage_multiplier": 4.8,
        "life_booster": 1.7,
        "lucky_charm": 1.7,
        "acquisition": "Shop",
        "price": 3700000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/f/f9/Uo_Uo_no_Mi%2C_Model_Seiryu_Infobox.png/revision/latest?cb=20211204205430"
    },
    {
        "Eng_name": "Bird-Bird Fruit, Model: Phoenix",
        "name": "Tori Tori no Mi, Model: Phoenix",
        "type": "Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a phoenix.",
        "damage_multiplier": 4.6,
        "life_booster": 1.6,
        "lucky_charm": 1.6,
        "acquisition": "Shop",
        "price": 3400000,
        "image_url": "https://static.wikia.nocookie.net/onepiecefanon/images/6/68/Phoenix_Infobox.jpeg/revision/latest?cb=20220804144824"
    },
    {
        "Eng_name": "Dog-Dog Fruit, Model: Wolf Mythical Type: Okuchi no Makami",
        "name": "Inu Inu no Mi, Model: Okuchi no Makami",
        "type": "Mythical Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a wolf deity.",
        "damage_multiplier": 4.4,
        "life_booster": 1.5,
        "lucky_charm": 1.5,
        "acquisition": "Shop",
        "price": 3100000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/1/1d/Inu_Inu_no_Mi%2C_Model_Okuchi_no_Makami_Infobox.png/revision/latest?cb=20221120062131"
    },
    {
        "Eng_name": "Human-Human Fruit, Model: Great Buddha",
        "name": "Hito Hito no Mi, Model: Daibutsu",
        "type": "Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a colossal Buddha statue.",
        "damage_multiplier": 4.2,
        "life_booster": 1.4,
        "lucky_charm": 1.4,
        "acquisition": "Shop",
        "price": 2800000,  # Larger and more powerful transformation justifies a higher price
        "image_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8dfb2bae-bb02-4067-839c-1f66e0f41f34/d6ndir1-8205630a-a43e-41f4-9fe2-ffb56af8cece.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhkZmIyYmFlLWJiMDItNDA2Ny04MzljLTFmNjZlMGY0MWYzNFwvZDZuZGlyMS04MjA1NjMwYS1hNDNlLTQxZjQtOWZlMi1mZmI1NmFmOGNlY2UucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.eUx97VxNVULQz20TwdIVxy3xWswZv9wNrxc1vukeKuQ"
    },
    {
        "Eng_name": "Serpent-Serpent Fruit, Model: Eight-Headed Serpent",
        "name": "Hebi Hebi no Mi, Model: Yamata no Orochi",
        "type": "Zoan",
        "ability": "Allows users to transform into a hybrid or full form of an eight-headed serpent.",
        "damage_multiplier": 4.0,
        "life_booster": 1.8,
        "acquisition": "Shop",
        "price": 2500000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/3/3e/Hebi_Hebi_no_Mi%2C_Model_Yamata_no_Orochi_Infobox.png/revision/latest?cb=20210307032049"
    },
    {
        "Eng_name": "Dog-Dog Fruit, Model: Nine-Tailed Fox",
        "name": "Inu Inu no Mi, Model: Kyubi no Kitsune",
        "type": "Mythical Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a nine-tailed fox spirit.",
        "damage_multiplier": 3.8,
        "life_booster": 1.7,
        "acquisition": "Shop",
        "price": 2200000,
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/5/57/Inu_Inu_no_Mi%2C_Model_Kyubi.png/revision/latest?cb=20201109063837"
    },
    {
        "Eng_name": "Dragon-Dragon Fruit, Model: Pteranodon",
        "name": "Ryu Ryu no Mi, Model: Pteranodon",
        "type": "Ancient Zoan",
        "ability": "Allows users to transform into a hybrid or full form of a pteranodon.",
        "damage_multiplier": 3.6,
        "life_booster": 1.6,
        "acquisition": "Shop",
        "price": 1900000,
        "image_url": "https://static.wikia.nocookie.net/oproleplaying/images/0/0c/Anim_Zoan.png/revision/latest?cb=20220129203114"
    },
    {
        "Eng_name": "Dragon-Dragon Fruit, Model: Brachiosaurus",
        "name": "Ryu Ryu no Mi, Model: Brachiosaurus",
        "type": "Ancient Zoan",
        "ability": "Allows users to transform into a Brachiosaurus, an ancient herbivorous dinosaur.",
        "damage_multiplier": 3.4,
        "life_booster": 1.5,
        "acquisition": "Shop",
        "price": 1600000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/5/58/Ryu_Ryu_no_Mi%2C_Model_Triceratops_Beast_Form.png/revision/latest/smart/width/386/height/259?cb=20220529042151"
    },
    {
        "Eng_name": "Cat-Cat Fruit, Model: Leopard",
        "name": "Neko Neko no Mi, Model: Leopard",
        "type": "Zoan",
        "ability": "Allows users to transform into a leopard.",
        "damage_multiplier": 3.2,
        "life_booster": 1.4,
        "acquisition": "Shop",
        "price": 1300000,
        "image_url": "https://static.wikia.nocookie.net/onepiece/images/9/98/Neko_Neko_no_Mi%2C_Model_Leopard_Infobox.png/revision/latest?cb=20230306213909"
    },
    {
        "Eng_name": "Bull-Bull Fruit, Model: Giraffe",
        "name": "Ushi Ushi no Mi, Model: Giraffe",
        "type": "Zoan",
        "ability": "Allows users to transform into a giraffe.",
        "damage_multiplier": 3.0,
        "acquisition": "Shop",
        "price": 1000000,
        "image_url": "https://img2.cgtrader.com/items/3795174/976e12b866/large/ushi-ushi-no-mi-model-giraffe-one-piece-devil-fruit-3d-model-976e12b866.jpg"
    },
    {
        "Eng_name": "Elephant-Elephant Fruit, Model: Mammoth",
        "name": "Zou Zou no Mi, Model: Mammoth",
        "type": "Zoan",
        "ability": "Allows users to transform into a mammoth.",
        "damage_multiplier": 2.8,
        "acquisition": "Shop",
        "price": 700000,
        "image_url": "https://static.wikia.nocookie.net/king-piece/images/d/d3/MammothFruit.png/revision/latest?cb=20220501202527"
    }
]

def setup(bot):

    @bot.command(name="buy")

    async def buy_fruit(ctx, *, fruit_name: str):
        fruit = next((f for f in devil_fruits if f["name"].lower() == fruit_name.lower()), None)

        if fruit:
            user_id = ctx.author.id
            db_cursor.execute("SELECT berries FROM treasure WHERE user_id = ?", (user_id,))
            user_berries = db_cursor.fetchone()[0]

            if user_berries >= fruit["price"]:
                db_cursor.execute("UPDATE treasure SET berries = berries - ? WHERE user_id = ?", (fruit["price"], user_id))
                db_connection.commit()

                # Check if the user already has a devil fruit
                db_cursor.execute("SELECT * FROM user_devil_fruits WHERE user_id = ?", (user_id,))
                existing_devil_fruit = db_cursor.fetchone()

                if existing_devil_fruit:
                    await ctx.send("You already have a devil fruit. Use the current one before buying a new one.")
                else:
                    # Insert the new devil fruit into the user_devil_fruits table
                    db_cursor.execute("INSERT INTO user_devil_fruits (user_id, devil_fruit) VALUES (?, ?)", (user_id, fruit["name"]))
                    db_connection.commit()

                    await ctx.send(f"You've bought {fruit['name']} for <:image:1141659940109418557>{fruit['price']}!")

            else:
                await ctx.send("You don't have enough berries to buy this fruit.")
        else:
            await ctx.send("That fruit doesn't exist.")

    @bot.command(name="drop")
    async def drop(ctx, cost: int):
        if cost not in [100, 1000, 10000]:
            await ctx.send("Invalid cost. Please choose from 100, 1000, or 10000.")
            return

        devil_fruit_to_drop = get_random_devil_fruit_in_range(cost)
        if devil_fruit_to_drop is None:
            await ctx.send("No devil fruit available in the specified cost range.")
            return

        user_id = ctx.author.id
        db_cursor.execute("SELECT berries FROM treasure WHERE user_id = ?", (user_id,))
        user_berries = db_cursor.fetchone()[0]

        if user_berries >= cost:
            db_cursor.execute("UPDATE treasure SET berries = berries - ? WHERE user_id = ?", (cost, user_id))
            db_cursor.execute("UPDATE user_devil_fruits SET devil_fruit = ? WHERE user_id = ?", (devil_fruit_to_drop["name"], user_id))
            db_connection.commit()

            embed = discord.Embed(title="Dropped Devil Fruit", color=discord.Color.green())
            embed.set_thumbnail(url=devil_fruit_to_drop["image_url"])
            embed.add_field(name="Name", value=devil_fruit_to_drop["name"], inline=False)
            embed.add_field(name="Type", value=devil_fruit_to_drop["type"], inline=True)
            embed.add_field(name="Ability", value=devil_fruit_to_drop["ability"], inline=True)
            embed.add_field(name="Price", value=f"{cost} Berry", inline=True)

            await ctx.send(embed=embed)
        else:
            await ctx.send("You don't have enough berries to purchase this dropped devil fruit.")

        db_cursor.execute("DELETE FROM user_devil_fruits WHERE user_id = ? AND devil_fruit = ?", (user_id, devil_fruit_to_drop["name"]))
        db_connection.commit()


    def get_random_devil_fruit_in_range(cost):
        valid_devil_fruits = [devil_fruit for devil_fruit in devil_fruits if cost_range_includes_cost(devil_fruit, cost)]
        if valid_devil_fruits:
            return random.choice(valid_devil_fruits)
            # Before the line causing the KeyError
            print("Valid Devil Fruits:", valid_devil_fruits)
        return None

    def cost_range_includes_cost(devil_fruit, cost):
        return devil_fruit["price"] >= cost_range_min(cost) and devil_fruit["price"] <=   cost_range_max(cost)

    def cost_range_min(cost):
        return {
            100: 0,
            1000: 100,
            10000: 1000
        }[cost]

    def cost_range_max(cost):
        return {
            100: 1000,
            1000: 10000,
            10000: 100000
        }[cost]

    @bot.command(name="df")
    async def devil_fruit_info(ctx, *, fruit_name: str):
        fruit_name = fruit_name.strip()  # Remove leading and trailing spaces
        fruit_lower = fruit_name.lower()  # Store lowercase name for comparison
    
        matching_fruits = [
            f for f in devil_fruits if fruit_lower in f["name"].lower()
        ]
    
        if matching_fruits:
            embed = discord.Embed(title="Matching Devil Fruits",
                              color=discord.Color.random())
            for fruit in matching_fruits:
                
                
                if "life_booster" in fruit:
                    if "lucky_charm" in fruit:
                        embed.add_field(
                            name=fruit["name"],
                            value=(
                                f"**English Name:** {fruit['Eng_name']}\n"
                                f"**Type:** {fruit['type']}\n"
                                f"**Ability:** {fruit['ability']}\n"
                                f"**Damage Multiplier:** {fruit['damage_multiplier']}\n"
                                f"**Life Booster:** {fruit['life_booster']}\n"
                                f"**Lucky Charm:** {fruit['lucky_charm']}\n"
                                f"**Price:** <:image:1141659940109418557>{fruit['price']}"
                            ),
                            inline=False
                        )
                    else :
                        embed.add_field(
                            name=fruit["name"],
                            value=(
                                f"**English Name:** {fruit['Eng_name']}\n"
                                f"**Type:** {fruit['type']}\n"
                                f"**Ability:** {fruit['ability']}\n"
                                f"**Damage Multiplier:** {fruit['damage_multiplier']}\n"
                                f"**Life Booster:** {fruit['life_booster']}\n"
                                f"**Price:** <:image:1141659940109418557>{fruit['price']}"
                            ),
                            inline=False
                        )
                else:
                    embed.add_field(
                        name=fruit["name"],
                        value=(
                            f"**English Name:** {fruit['Eng_name']}\n"
                            f"**Type:** {fruit['type']}\n"
                            f"**Ability:** {fruit['ability']}\n"
                            f"**Damage Multiplier:** {fruit['damage_multiplier']}\n"
                            f"**Price:** <:image:1141659940109418557>{fruit['price']}"
                        ),
                        inline=False
                    )
                    
            embed.set_thumbnail(url=matching_fruits[0]["image_url"])
            await ctx.send(embed=embed)
        else:
            await ctx.send("No matching fruits found.")
