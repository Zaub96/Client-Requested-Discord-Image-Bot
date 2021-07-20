import discord
from discord.ext import commands
import random as r
import os

#feature to add
#submit text thats saved to a file that takes user input and gives me a list with name of user and their suggested feature
#automization
#put file on "cooldown"
#search for the word juicers itself

dbt=open(r"C:\\Users\\zacha\\AppData\\Local\\Programs\\Python\\Python36\\Projects\\DiscordBotTag.txt" , "r")
FP = r"C:\\Users\\zacha\\AppData\\Local\\Programs\\Python\\Python36\\Projects\\Juicers\\"
X = os.listdir(FP)
os.getcwd()
client = commands.Bot(command_prefix = 'j')

@client.event  
async def on_ready():
    print('Juicers Inbound')

@client.command()
async def ping(ctx):    
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def uicers(ctx):
    randoFile = r.choice(X)
    await ctx.send((f'DM submissions to Deleto'), file=discord.File(FP+randoFile))

#specify if an image has 2B (filename?)
#if so figure out how to @Fun_Size

client.run(dbt.read())