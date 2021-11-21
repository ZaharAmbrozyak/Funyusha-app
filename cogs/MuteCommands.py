import asyncio
from discord.ext import commands
from my_converters import DurationConverter
import asyncio
import discord

class MuteCommands(commands.Cog):
     '''Команды, для манипуляции с мутами'''
     def __init__(self, client):
         self.client = client

     @commands.command(aliases = ['mute'])
     @commands.has_permissions(manage_messages=True)
     async def мут(self, ctx, member: commands.MemberConverter, *, reason=None):
          '''|Няша замутит указаного пользователя!'''
          guild = ctx.guild
          mutedRole = discord.utils.get(guild.roles, name="Muted")

          if not mutedRole:
               mutedRole = await guild.create_role(name='Muted')
               for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)
          
          await member.add_roles(mutedRole, reason=reason)
          await ctx.send(f"{member.mention} замучен, по причине {reason}")
          await member.send(f"Ты был замучен на сервере {guild.name} по причине {reason}. Я напишу тебе, когда тебя размутят.")

     @commands.command(aliases = ["темпмут", 'tempmute','tmute','тмут',"временныймут"])
     @commands.has_permissions(manage_messages=True)
     async def времмут(self, ctx, member: commands.MemberConverter, duration : DurationConverter, *, reason=None):
          '''|Няша замутит пользоваталя на указаное время!'''
          multiplier = {'s': 1, 'm': 60, 'h': 3600}
          amount, unit = duration

          guild = ctx.guild
          mutedRole = discord.utils.get(guild.roles, name="Muted")

          if not mutedRole:
               mutedRole = await guild.create_role(name='Muted')
               for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)
          
          await member.add_roles(mutedRole)
          await ctx.send(f"{member.mention} Замучен на {amount}{unit}, по причине {reason}")
          await member.send(f"Ты был замучен на сервере {guild.name} на {amount}{unit} по причине {reason}. Я напишу тебе, когда тебя размутят.")
          await asyncio.sleep(amount * multiplier[unit])
          await member.remove_roles(mutedRole)
          await member.send(f"Ты был размучен на сервере {guild.name}.")
     
     @commands.command(aliases = ['unmute','размутить',"анмут"])
     @commands.has_permissions(manage_messages=True)
     async def размут(self, ctx, member: commands.MemberConverter):
          '''|Няша размутит указаного пользователя!'''
          mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
          await member.remove_roles(mutedRole)
          await ctx.send(f"{member.mention} размучен")
          await member.send(f"Ты был размучен на сервере {ctx.guild.name}.")

def setup(client):
     client.add_cog(MuteCommands(client))