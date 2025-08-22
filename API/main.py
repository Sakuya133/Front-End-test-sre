import discord
import random
import aiohttp
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def diskon(ctx):
    games = {
        "LEGO: The Hobbit": "285160",
        "Elden Ring": "1245620"
    }

    try:
        async with aiohttp.ClientSession() as session:
            messages = []
            for title, appid in games.items():
                async with session.get(f"https://store.steampowered.com/api/appdetails?appids={appid}") as resp:
                    data = await resp.json()
                    game_data = data.get(appid, {})
                    if game_data.get("success"):
                        info = game_data["data"]
                        price = info.get("price_overview")
                        if price:
                            messages.append(
                                f" **{title}**\n Harga: {price['final_formatted']} (Diskon: {price['discount_percent']}%)\n"
                            )
            await ctx.send("\n".join(messages))

    except Exception as e:
        await ctx.send("bruh")
        print("Diskon Error:", e)


# perintah dibawah merupakan bot token discord, untuk diaktifkan bisa menggunakan discord developer mode
# You can get the token from the Discord Developer Portal:
# https://discord.com/developers/applications
bot.run('token bot discord')
