import discord
from discord.ext import commands
from ek_calisma import yazı_tura
from ders2_1 import sifre_olusturucu

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def toplama(ctx,a = 1, b = 2):
    await ctx.send(a + b)

@bot.command()
async def carpma(ctx,a = 1, b = 2):
    await ctx.send(a * b)

@bot.command()
async def yazı_tura_o(ctx):
    await ctx.send(yazı_tura())


bot.run("MTE3NDM4NTQ0ODY1OTk4ODYxMQ.GCUHpA.Lw_n4hzob-d4IsjsID-0n6p_sHgiDn2c7iV5pU")
