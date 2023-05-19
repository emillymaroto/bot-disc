import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def fica(ctx, member: discord.Member):
  await ctx.send(f'fica quietinho para eu gostar de vc, {member.mention}!')


bot.run(
  ')
