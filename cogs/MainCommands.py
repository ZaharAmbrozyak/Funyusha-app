from discord.ext import commands
from discord.ext.commands.core import command

class MainCommands(commands.Cog):
     '''События для бота!'''
     def __init__(self, client):
          self.client = client

  

     @commands.Cog.listener()
     async def on_ready(self):
          '''When bot is ready'''
          print(f'Bot is logged in as {self.client.user}!')
     
     @commands.Cog.listener()
     async def on_message(self, message):
          '''Print message (log)'''
          print(f"{message.author}: {message.content}")
     
def setup(client):
     '''cog setup'''
     client.add_cog(MainCommands(client))