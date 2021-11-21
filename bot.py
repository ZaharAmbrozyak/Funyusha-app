from discord.ext import commands
from os import listdir, environ
from discord import Intents, Activity

status = '?help'
bot = commands.Bot(command_prefix='?', owner_id=566676330427449364, intents = Intents.all(),
          description="Бот Няша предоставляет большое количество возможностей!",
          activity=Activity(type=1, name=status, url='https://www.youtube.com/watch?v=kNOZcr6Iifs'))

@bot.command(aliases=['load'])
@commands.is_owner()
async def загрузить(ctx, extension: str='MainCommands') -> None:
     '''|Загружает разширение'''
     bot.load_extension(f"cogs.{extension}")
     await ctx.message.reply(f"Разширение '{extension}' загружено успешно!")

@bot.command(aliases=['unload'])
@commands.is_owner()
async def выгрузить(ctx, extension: str='MainCommands') -> None:
     '''|Убирает разширение'''
     bot.unload_extension(f"cogs.{extension}")
     await ctx.message.reply(f"Разширение '{extension}' выгружено успешно!")

@bot.command(aliases=['reload'])
@commands.is_owner()
async def перезагрузить(ctx, extension: str='MainCommands') -> None:
     '''|Перезагружает разширение''' 
     bot.unload_extension(f"cogs.{extension}")
     bot.load_extension(f"cogs.{extension}")
     await ctx.message.reply(f"Разширение '{extension}' перезагружено успешно!")

[bot.load_extension(f'cogs.{filename[:-3]}') for filename in listdir('./cogs') if filename.endswith('.py')]

if __name__ == '__main__':
     bot.run(environ.get('TOKEN'))