def main():
    cogname = input("  The classes name: ")
    botname = input("  Your bot instance's name: ")

    code = f"""
import discord
import asyncio
from discord.ext import commands 


class {cogname}(commands.Cog):
    def __init__(self, {botname}):
        self.{botname} = {botname}
    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{cogname} has been loaded.")
        
    
    
    
    
    def setup({botname}):
        {botname}.add_cog({cogname}({botname}))"""

    with open(f"{cogname}.py", "w") as f:
        f.write(code)

    input(f"{cogname} has been successfully created.")

main()