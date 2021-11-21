from discord.ext import commands
from random import choice, randint
from sys import path

path.insert(0, '../')
from variables import responses, joke, where


class Utilities(commands.Cog):
     '''Список команд-утилит, которые могут помочь вам в некоторых ситуациях'''
     def __init__(self, client):
         self.client = client

     @commands.command(aliases=['8ball', 'ball', '8b'])
     async def шар(self, ctx, *, question):
          '''|Задайте вопрос, ответ на который Да или Нет. Няша даст вам на него ответ!'''
          await ctx.send(f'{choice(responses)}')
     
     @commands.command()
     async def шип(self, ctx):
          '''Рандомный шип'''
          player1 = choice(list(filter(lambda x: x.bot != True,ctx.guild.members)))
          player2 = choice(list(filter(lambda x: x != player1 and x.bot != True, ctx.guild.members)))

          await ctx.send(f"Рандомный шип:\n💕{player1.name}💕{player2.name}💕\nЛюбите друг друга!")

     @commands.command(alieses=['coin',"коин","монета"])
     async def монетка(self, ctx):
          '''|Что выпадет, орёл, или решка? Няша даст ответ!'''
          chance = randint(0,101)
          if chance < 50:
               await ctx.send("Орёл!")
          elif chance < 99:
               await ctx.send("Решка!")
          else:
               await ctx.send("Ребро!")
     
     @commands.command(alieses=['ping'], help='Показывает пинг няшки\n?ping', )
     async def пинг(self, ctx):
          '''|Показывает пинг няшки'''
          await ctx.send(f"Пинг!{round(self.client.latency * 1000)}ms")
     
     @commands.command(alieses=['random','rand', 'рандом', "ранд"], help='Введите числа от и до, и няша даст вам рандомное число из этого списка!\nПримеры:\n?rand 100 200\n?random 200')
     async def ранд(self, ctx, min, max=0):
          '''|Введите числа от и до, и няша даст вам рандомное число из этого списка!'''
          if max:
               await ctx.send(f"{randint(int(min), int(max))}")
          else:
               await ctx.send(f"{randint(int(0), int(min))}")
     
     @commands.command(aliases=['chance'], help='Няша скажет шанс на событие которое вы напишите\nНапример\n?шанс С каким шансом фан пойдёт делать бота?\n', brief='Няша скажет шанс на событие которое вы напишите')
     async def шанс(self, ctx, *, text):
          "|Няша скажет шанс на событие которое вы напишите"
          num = randint(0,100)
          float = randint(0,9999)
          if num == 100:
               await ctx.send(f"%СТО%ПРОЦЕНТОВ%")
          elif num == 0 and float == 0:
               await ctx.send("Поздравляем!Вы выбили ПОЛНЫЙ НОЛЬ! 0,0000%!")
          else:
               await ctx.send(f"Я думаю, шанс {num}.{float}%")  
     
     @commands.command()
     async def шутка(self, ctx):
          member1 = choice(list(filter(lambda x: x.bot != True,ctx.guild.members)))
          member2 = choice(list(filter(lambda x: x != member1 and x.bot != True, ctx.guild.members)))

          converter = commands.TextChannelConverter()
          channel = await converter.convert(ctx, str(885403370570014740))
          
          messages = []
          async for message in channel.history():
               messages.append(message)
          
          message = choice(messages)

          await ctx.send(f"{choice(where)} {member1.name} и {member2.name}. {member1.name} расказывает шутку: \n\n{message.content}\n\n{member2.name} после этого отвечает: \n-{choice(joke)}")

def setup(client):
     client.add_cog(Utilities(client))
