from discord.ext import commands
import discord
from PIL import Image
from io import BytesIO

class ASCII(commands.Cog):
     '''Манипуляция с ASCII кодировкой'''
     def __init__(self, client):
         self.client = client
         self.ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ":", ',', '.']
     
     def resize_image(self, image, new_width=100):
          width, height = image.size
          ratio = height / width
          new_height = int(new_width * ratio)
          resized_image = image.resize((new_width, new_height))
          return(resized_image)
     
     def grayify(self, image):
          grayscale_image = image.convert('L')
          return(grayscale_image)

     def pixels_to_ascii(self, image):
          pixels = image.getdata()
          characters = ''.join([self.ASCII_CHARS[pixel//25] for pixel in pixels])
          return(characters)

     @commands.command(aliases=['to_ascii', 'toascii'])
     async def ascii(self, ctx, member: commands.MemberConverter = None):
          if member is None:
               member = ctx.author
          
          asset = member.avatar_url_as()
          data = BytesIO(await asset.read())
          image = Image.open('images/profile.jpg')

          new_width = 100

          new_image_data = self.pixels_to_ascii(self.grayify(self.resize_image(image)))

          pixel_count = len(new_image_data)
          ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count))

          with open('txt files/ascii_image.txt', 'w') as f:
               f.write(ascii_image)

          await ctx.send(file=discord.File('txt files/ascii_image.txt'))

          

          


def setup(client):
     client.add_cog(ASCII(client))