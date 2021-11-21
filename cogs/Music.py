from variables import available_mp3_files
import discord
from functions import can_do_music_command
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):
     '''Команды для музыки'''
     def __init__(self, client):
          self.client = client

     @commands.command(aliases=['join', 'connect', "ввойти"])
     async def зайти(self, ctx):
          '''|Няша зайдёт в войс в котором вы находитесь'''
          if ctx.author.voice is None:
               await ctx.send("Ты не в войсе!")
          else:
               voice_channel = ctx.author.voice.channel
               if ctx.voice_client is None:
                    await voice_channel.connect()
               else:
                    await ctx.voice_client.move_to(voice_channel)
     
     @commands.command(aliases=['disconnect', 'leave', 'exit'])
     @commands.check(can_do_music_command)
     async def выйти(self, ctx):
          '''|Няша выйдет из войса'''
          await ctx.voice_client.disconnect()
     
     @commands.group(aliases=['play','playmusic'], invoke_without_command=True)
     @commands.check(can_do_music_command)
     async def играть(self, ctx):
          await ctx.send("Введи аргументы youtube или file")

     @играть.command(name='youtube')
     async def youtube_play(self, ctx, url):
          '''|Няша заиграет песню, из ссылки ютуба'''
          ctx.voice_client.stop()
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          YDL_OPTIONS = {'format': "bestaudio"}
          vc = ctx.voice_client

          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
               info = ydl.extract_info(url, download=False)
               url2 = info['formats'][0]['url']
               source = await discord.FFmpegOpusAudio.from_probe(source=url2, executable='ffmpeg_executable/ffmpeg.exe', **FFMPEG_OPTIONS)

               vc.play(source)

     @играть.command(name='file', help=f'Все возможные аргументы к команде игратьф:\n{available_mp3_files}')
     @commands.check(can_do_music_command)
     async def file_play(self, ctx, filename: str):
          '''|Няша заиграет песню, из файла'''
          ctx.voice_client.stop()
          # FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          vc = ctx.voice_client
          if filename.endswith('.mp3'):
               filenamepath = f'audio/{filename}'
          else:
               filenamepath = f"audio/{filename}.mp3"
               
          source = await discord.FFmpegOpusAudio.from_probe(filenamepath, executable='ffmpeg_executable/ffmpeg.exe')
          await ctx.send(f"Играю файл {filename}!")
          vc.play(source)

     @commands.command(aliases=['pause','stop'])
     @commands.check(can_do_music_command)
     async def пауза(self, ctx):
          '''|Няша остановит песню'''
          await ctx.send("Пауза...")
          await ctx.voice_client.pause()    

     @commands.command(aliases=['resume','continue'])
     @commands.check(can_do_music_command)
     async def продолжить(self, ctx):
          '''|Няша продолжит играть песню'''
          await ctx.send("Продолжаем!")
          await ctx.voice_client.resume()
          

def setup(client):
     client.add_cog(Music(client))