# Made by Jack Seigerman
import discord
import send
import asyncio

TOKEN = 'REPLACE WITH TOKEN'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def send_message(message, user_message):
    user_message = user_message.lower()
    try:

        if user_message == "/schedule":
            await send.schedule(message)

    except Exception as e:
        print("/command error ", repr(e))


@client.event
async def on_ready():
    game = discord.Game('REPLACE WITH STATUS MESSAGE')
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f'{client.user} is now active')
    guild_count = len(client.guilds)
    print(f"Bot is connected to {guild_count} server(s):")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content
    await send_message(message, user_message)
    await asyncio.sleep(0.25)


client.run(TOKEN)
