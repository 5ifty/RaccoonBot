import random
import discord

from discord.ext import commands
from utils import lists, permissions, http, default

class lifegen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
   @commands.command(aliases=['lifegen'])
    async def lifeme(self, ctx):
        """ generate a random life """
        age = random.choice(lists.age)
        sex = random.choice(lists.sex)
        school = random.choice(lists.school)
        job = random.choice(lists.job)
        money = random.choice(lists.money)
        kids = random.choice(lists.kids)
        death = random.choice(lists.death)
        deathcause = random.choice(lists.deathcause)
        gay = random.choice(lists.gay)
        license = random.choice(lists.license)
        country = random.choice(lists.country)
        print('Made possible by 5ifty#4279')
        await ctx.send(f"***{ctx.author.name}'s Life story***\n{age} {sex} Born in {country}.\nYou have decided your sexualality; You are a {gay}.\n{school}.\n{license}\n{job}.\n{money}.\n{kids}.\n{death} because {deathcause}. \n `This was made by 5ifty#4279.")     
     
     
   def setup(bot):
   bot.add_cog(lifegen(bot))
