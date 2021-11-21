from discord.ext import commands
from my_converters import DurationConverter
from discord import Member
import typing
import asyncio

class BanCommands(commands.Cog):
     '''Class with commands for ban, unban, kick, etc...'''
     def __init__(self, client):
         self.client = client

     @commands.command(aliases=['ban'])
     @commands.has_permissions(ban_members=True)
     async def бан(self, ctx, members: commands.Greedy[Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str=None) -> None:
          '''|Bot will ban user(s)'''
          for member in members:
               await member.ban(delete_message_days=delete_days, reason=reason)
               await ctx.send(f"{member.mention} banned, for a reason {reason}.")
     
     @commands.command(aliases=['tempban', 'tban', 'вбан'],
          help='Bot will ban member(s) for a cartain period\nFor example:\n?ban example 1234567890098765321 example#1234')
     @commands.has_permissions(ban_members=True)
     async def врембан(self, ctx, members: commands.Greedy[Member], duration: DurationConverter, 
                    delete_days: typing.Optional[int] = 0, *, reason: str=None) -> None:
          '''| Bot will ban member(s) for a cartain period'''
          multiplier = {'s': 1, 'm': 60, 'h': 3600}
          amount, unit = duration

          for member in members:
               await member.ban(reason=reason, delete_days=delete_days)
               await ctx.send(f"{member.mention} was banned for {amount}{unit}, for reason {reason}.")
          for member in members:
               await asyncio.sleep(amount * multiplier[unit])
               await ctx.guild.unban(member)
               await ctx.send(f"{member.mention} was unbaned")
     
     @commands.command(aliases=['unban'])
     @commands.has_permissions(ban_members=True)
     async def разбан(self, ctx, *, member: commands.UserConverter) -> None:
          '''|Bot will mercy, and unban the user'''
          banned_users = await ctx.guild.bans()

          member_name, member_discriminator = member.split('#')

          for ban_entry in banned_users:
               user = ban_entry.user
               if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f"{user.name}#{user.descriminator} was unbanned.")
                    return
          await ctx.send(f"{member} was not found in a list of banned users.") 

     @commands.command(aliases=['kick'])
     @commands.has_permissions(kick_members=True)
     async def кик(self, ctx, members: commands.Greedy[Member], *,
                   reason: str=None) -> None:
          '''Bot will kick a user'''
          for member in members:
               await member.kick(reason=reason)
               await ctx.send(f"{member.mention} was kicked, for a reson {reason}.")

def setup(client):
     client.add_cog(BanCommands(client))