import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!")  # You can change "!" to anything

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.environ["DISCORD_TOKEN"])
