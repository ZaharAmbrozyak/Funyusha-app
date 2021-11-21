from discord.ext import commands
from variables import words_list
from random import choice


class HangMan(commands.Cog):
     '''Игра виселица!'''
     
     def __init__(self, client):
         self.client = client

     def get_word(self):
          word = choice(words_list)

          return word.upper()

     @commands.command()
     async def виселица(self, ctx):
          word = self.get_word()
          word_completion = "― " * len(word)
          guessed = False
          guessed_letters = []
          tries = 8
          
          await ctx.send(f"Давай поиграем в виселицу!\nЧтобы ввести букву, используйте ?inp\n{self.display_hangman(tries-1)}\n{word_completion}")

     def display_hangman(self, tries):
          stages = [ """
          
                         --------
                         |      |
                         |      O
                         |     \\|/
                         |      |
                         |     / \\
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |     \\|/
                         |      |
                         |     / 
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |     \\|/
                         |      |
                         |     
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |     \\|/
                         |      
                         |     
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |      |/
                         |      
                         |     
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |      |
                         |      
                         |     
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      O
                         |      
                         |      
                         |     
                         ―
                     """,
                     """
          
                         --------
                         |      |
                         |      
                         |      
                         |      
                         |     
                         ―
                     """
          ]
          return stages[tries]

def setup(client):
     client.add_cog(HangMan(client))