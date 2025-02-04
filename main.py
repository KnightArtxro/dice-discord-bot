import discord
from discord.ext import commands
import random
import os

my_secret = os.environ['TOKEN']
gif = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGJjZXI5eWpweTF5bnZsdXA3NHowa3RsYnNzZjQwMno1Zmo1MDNoeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bubpLP4o75fmIVukRr/giphy.gif"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix="/",
    intents=intents,
)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


@bot.command(name='d6')
async def lanzar_d6(ctx):
    resultado = random.randint(1, 6)

    # Crear un embed
    embed = discord.Embed(
        title=f"🎲 Resultado del dado: {resultado}",
        color=discord.Color.blue()  # Color del embed (opcional)
    )
    embed.set_image(url=gif)  # Mostrar el GIF en el embed

    # Enviar el embed
    await ctx.send(embed=embed)


@bot.command(name='d20')
async def lanzar_d20(ctx):
    resultado = random.randint(1, 20)
    gif = "https://media.giphy.com/media/rnbRo2ACilXJwCkijD/giphy.gif?cid=790b76112k3r2rkoo2zlmv80ptkuxsuxu5dnmyhb4hanbd2n&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    # Crear un embed
    embed = discord.Embed(
        title=f"🎲 Resultado del dado: {resultado}",
        color=discord.Color.blue()  # Color del embed (opcional)
    )
    embed.set_image(url=gif)  # Mostrar el GIF en el embed

    # Enviar el embed
    await ctx.send(embed=embed)

bot.run(my_secret)
