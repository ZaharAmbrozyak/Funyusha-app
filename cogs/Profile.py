from discord.ext import commands
from functions import load_file, write_file

class Profile(commands.Cog):
     def __init__(self, client):
          self.client = client
          self.filename = 'data.json'

     @commands.group(name='profile', invoke_without_command=True)
     async def profile(self, ctx) -> None:
          '''Команда профиль может записать дополнительную информацию о человеке на сервере.
             Команда профиль имеет несколько под функций для работы'''
          await ctx.send("Введите аргументы")

     @profile.command(name='change')
     async def change(self, ctx, *, text: str) -> None:
          '''Изменяет профиль учасника сервера'''
          member_id = str(ctx.author.id)
          server_id = str(ctx.guild.id)

          data = load_file(self.filename)

          if server_id in data.keys():
               data[server_id][member_id] = text
          else:
               data[server_id] = {}
               data[server_id][member_id] = text
          
          await ctx.send(f"Профиль изменён")
          
          write_file(self.filename, data)

     @profile.command(name='clear')
     async def clear(self, ctx) -> None:
          '''Очищает профиль учасника сервера'''
          member_id = str(ctx.author.id)
          server_id = str(ctx.guild.id)

          data = load_file(self.filename)

          if server_id in data.keys():
               data[server_id][member_id] = 'Профиль стёрт'

               await ctx.send("Профиль успешно очищен!")
          else:
               data[server_id] = {}
               data[server_id][member_id] = 'Профиля нету.'

               await ctx.send("Будьте внимательны! У вас нету профиля, чтобы его очищать!")
          
          write_file(self.filename, data)

     @profile.command(name='get')
     async def get(self, ctx) -> None:
          '''Отправляет профиль учасника сервера'''
          member_id = str(ctx.author.id)
          server_id = str(ctx.guild.id)

          data = load_file(self.filename)

          if server_id in data.keys() and member_id in data[server_id].keys():
               await ctx.send(data[server_id][member_id])
          else:
               await ctx.send("Профиля нету!")

def setup(client):
     client.add_cog(Profile(client))