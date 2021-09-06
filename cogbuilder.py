def main():
    cogname = input('  The classes name: ')
    code = f"""
import discord
import asyncio
from discord.ext import commands 


class {cogname.title()}(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cogname.title()} has been loaded.')
        
    
    
    
    
    def setup(bot):
        bot.add_cog({cogname}(bot))"""

    with open(f"{cogname}.py", "w") as f:
        f.write(code)

    input(f'{cogname.title()} cog has been successfully created.')

main()
