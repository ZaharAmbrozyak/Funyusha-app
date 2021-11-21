import discord
from discord.ext import commands

class Info(commands.Cog):
     '''Команда info которая покажет информацию чего-либо'''
     def __init__(self, client):
         self.client = client
         self.infoembed = None

     @commands.group(name='info', invoke_without_command=True)
     async def info(self, ctx):
          '''Инфа чего-то'''
          await ctx.send(f"Введи правильные аргументы, или поправь опечатку!\nВот список всех аргументов: member, role, message, guild, category, voice, emoji, channel")

     @info.command(name='member')
     async def user_embed(self, ctx, *, object: str=None):
          '''Кароче для юзеров инфа шаришь ок да'''
          converter = commands.MemberConverter()
          object = await converter.convert(ctx, object)
          user_name = f'{object.name}#{object.discriminator}'

          infoembed = discord.Embed(
               title = user_name,
               description = f'Аккаунт был создан в {object.created_at}',
               colour = object.colour
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_image(url=object.avatar_url)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
          
          infoembed.add_field(name='Лучшая роль', value=object.top_role, inline=True)
          infoembed.add_field(name='Статус', value=f'{object.desktop_status} - статус на пк\n', inline=True)
          infoembed.add_field(name='Активность', value=f'{object.activities}', inline=False)
          infoembed.add_field(name='Бусты на сервере', value=f'{user_name} забустил сервер в {object.premium_since}', inline=True)
          

          await ctx.send(embed=infoembed)
     
     @info.command(name='role')
     async def role_embed(self, ctx, *, object: str=None):
          '''Инфа роли'''
          converter = commands.RoleConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.name,
               description = f'Роль создана в {object.created_at}',
               colour = object.colour
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          await ctx.send(embed=infoembed)

     @info.command(name='guild')
     async def guild_embed(self, ctx):
          '''Информация о гильдии'''
          object = ctx.guild

          infoembed = discord.Embed(
               title = object.name,
               description = f'Сервер был создан в {object.created_at}',
               colour = discord.Colour.red()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_image(url=object.icon_url)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Description', value=object.description)
          infoembed.add_field(name='Large', value=object.large)
          infoembed.add_field(name='AFK channel', value=object.afk_channel.name)
          infoembed.add_field(name='Max Members', value=object.max_members)
          infoembed.add_field(name='Member count', value=object.member_count)
          infoembed.add_field(name='Region', value=object.region)

          await ctx.send(embed=infoembed)

     @info.command(name='message')
     async def message_embed(self, ctx, *, object: str=None):
          '''Инфа об сообщении'''
          converter = commands.MessageConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.author.display_name,
               description = f'Сообщение отправлено в {object.created_at}',
               colour = discord.Colour.green()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Content', value=object.content)
          infoembed.add_field(name='Channel', value=object.channel)
          infoembed.add_field(name='Guild', value=object.guild)

          await ctx.send(embed=infoembed)

     @info.command(name='category')
     async def category_embed(self, ctx, *, object: str=None):
          '''Информация об категории'''
          converter = commands.CategoryChannelConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.name,
               description = f'Категория была создана в {object.created_at}',
               colour = discord.Colour.orange()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Guild', value=object.guild)

          await ctx.send(embed=infoembed)

     @info.command(name='emoji')
     async def emoji_embed(self, ctx, *, object: str=None):
          '''Инфа смайла!'''
          converter = commands.EmojiConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.name,
               description = f'Роль была создана в {object.created_at}',
               colour = discord.Colour.dark_theme()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_image(url=object.url)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Guild', value=object.guild)
          infoembed.add_field(name='Is animated', value=object.animated)

          await ctx.send(embed=infoembed)

     @info.command(name='voice')
     async def voice_embed(self, ctx, *, object: str=None):
          '''Инфа войс канала'''
          converter = commands.VoiceChannelConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.name,
               description = f'Войс канал был создан в {object.created_at}',
               colour = discord.Colour.dark_gold()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Guild', value=object.guild)

          await ctx.send(embed=infoembed)

     @info.command(name='channel')
     async def channel_embed(self, ctx, *, object: str=None):
          '''Инфа текстового канала'''
          converter = commands.TextChannelConverter()
          object = await converter.convert(ctx, object)

          infoembed = discord.Embed(
               title = object.name,
               description = f'Канал был создан в {object.created_at}',
               colour = discord.Colour.purple()
          )

          infoembed.set_footer(text=object.id)
          infoembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

          infoembed.add_field(name='Guild', value=object.guild.name)
          infoembed.add_field(name='Category', value=object.category.name)
          # infoembed.add_field(name='Last Message', value=object.last_message.content)

          await ctx.send(embed=infoembed)

def setup(client):
     client.add_cog(Info(client))