import discord
import asyncio


async def schedule(message):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟', '⏸️', '❌', '❓']
    for day in days:
        embed = discord.Embed(title=day)
        day = await message.channel.send(embed=embed)
        for emote in emojis:
            await day.add_reaction(emote)
            await asyncio.sleep(0.5)
