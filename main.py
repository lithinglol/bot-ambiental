import discord
from discord.ext import commands
import random
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}!')

@bot.command()
async def tipos(ctx):
    await ctx.send("Los dos tipos principales de residuos son: Orgánicos e Inorgánicos")

@bot.command()
async def organicos(ctx):
    await ctx.send("Los residuos organicos son los que se pueden descomponer biológicamente, por ejemplo: residuos vegetales o desechos de animales")
    img = os.listdir('organic')
    ran = random.choice(img)
    with open(f'organic/{ran}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def inorganicos(ctx):
    await ctx.send("Los residuos inorganicos son los que no se pueden descomponer biológicamente, por ejemplo: plastico, metales o vidrio")
    img = os.listdir('inorganic')
    ran = random.choice(img)
    with open(f'inorganic/{ran}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def random_stat(ctx):
    ran = random.randint(1,4)
    if ran == 1:
        await ctx.send("Según la Organización Mundial de la Salud (OMS), el 99% de la población mundial respira aire contaminado.")
    elif ran == 2:
        await ctx.send("En 2021, la contaminación atmosférica causó 8,1 millones de muertes en todo el mundo.")
    elif ran == 3:
        await ctx.send("En México, se recolectan diariamente 103 millones de kilogramos de residuos urbanos.")
    elif ran == 4:
        await ctx.send("En 2022, se recibieron en México 6,047 kilogramos de material eléctrico y electrónico, 5,231 kilogramos de otros materiales, 2,169 kilogramos de llantas y 1,626 kilogramos de otros plásticos.")

@bot.command()
async def ayuda(ctx):
    with open(f'comandos.txt', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        text = discord.File(f)
    await ctx.send(file=text)

bot.run("*tu token aqui*")
