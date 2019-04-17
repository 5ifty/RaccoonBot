
import random
import discord

from discord.ext import commands

class coinflips(commands.Cog)
  def __init__(self, bot):
    self.bot = bot
    




@commands.command(alisases=['flip'])
    async def coinflip(self, ctx):
        coin = random.choice(coinoutcome.coin)
        await ctx.send(f" {ctx.author.mention} The coin landed on **{coin}**")
        
        
        
def setup(bot):
  bot.add_cog(coinflips)(bot))
        
        
        
