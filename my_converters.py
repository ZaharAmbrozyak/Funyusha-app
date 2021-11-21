from discord.ext import commands

class DurationConverter(commands.Converter):
     async def convert(self, ctx, argument):
          amount = argument[:-1]
          unit = argument[-1]
               
          if amount.isdigit() and unit in ['s', 'm', 'h']:
               return (int(amount), unit)
               
          raise commands.BadArgument(message='Bad duration')