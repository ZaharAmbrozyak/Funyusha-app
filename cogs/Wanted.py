import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

class Wanted(commands.Cog):
     '''Плакат Wanted!'''
     def __init__(self, client):
          self.client = client
     
     @commands.command(aliases=['нужен'])
     async def wanted(self, ctx, *, member: commands.MemberConverter = None):
          '''Сделает постер: "Нужен живой или мёртвый" из указаного пользователя'''
          if member is None:
               member = ctx.author
               
          wanted = Image.open('images/wanted.jpg')

          asset = member.avatar_url_as(size = 128)
          data = BytesIO(await asset.read())
          pfp = Image.open(data)

          pfp = pfp.resize((386, 386))

          wanted.paste(pfp, (98, 217))

          wanted.save('images/profile.jpg')

          await ctx.send(file=discord.File('images/profile.jpg'))

def setup(client):
     client.add_cog(Wanted(client))
