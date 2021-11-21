from discord.ext import commands
import asyncio
from my_converters import DurationConverter

class Administrator(commands.Cog):
     '''Команды, доступные только людьми с определёнными правами'''
     def __init__(self, client):
         self.client = client
                   
     @commands.command(aliases=['clean', 'очистить'], help='Няша очистит указанное количество сообщений в чате!\nНапример:\n?clear 10\n', 
                       brief='|Няшка очистит указанное количество сообщений в чате!')
     @commands.has_permissions(manage_messages=True)
     async def clear(self, ctx, amount: int = 2) -> None:
          '''|Bot will clean messages that you need'''
          await ctx.channel.purge(limit=amount)
          await ctx.send(f"{amount} was deleted")
     
     @commands.command(aliases=['времроль'], brief='Няша даст временно роль человеку',
          help='Няша выдаст определённую роль пользователю на определённое время.\nНапример:\n?времроль Няша 761643941426364448 1h\n')
     @commands.has_permissions(manage_roles=True)
     async def temprole(self, ctx, member: commands.MemberConverter, role: commands.RoleConverter, duration: DurationConverter) -> None:
          '''Bot will give role to member for a cantain duration'''
          multiplier = {'s': 1, 'm': 60, 'h': 3600}
          amount, unit = duration

          await member.add_roles(role)
          await ctx.send(f"{member.mention}, пользователь под ником {ctx.author.mention} выдал тебе роль {role.name} на {amount}{unit}! :)")
          await asyncio.sleep(amount * multiplier[unit])
          await member.remove_roles(role)
          await ctx.send(f"{member.mention}, время роли {role.name} истекло, поэтому я её убираю...")
     
     @commands.command(aliases=['повторить'])
     @commands.has_permissions(administrator=True)
     async def repeat(self, ctx, count: int=2, *, message: str) -> None:
          '''Bot will repeat messages n times'''
          [await ctx.send(message) for i in range(0, count)]

def setup(client):
     client.add_cog(Administrator(client))
