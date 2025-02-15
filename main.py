import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yapıldı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Mesajın bir komut olup olmadığını kontrol etme
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        # Alınan mesajı geri gönderme
        await message.channel.send(message.content)

# about komutu için bir işleyici ekleme
@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py ile oluşturulmuş basit bir bot!')

@client.command()
async def secim(ctx, *secmeler):
    # *secmeler ile gelen tüm seçeneklerden birini rastgele seçiyoruz
    x = random.choice(secmeler)
    await ctx.send(f"Seçimim: {x}")

client.run("MTI0OTc0NzI2NzgyMTUwNjY0Mg.Gi7bdD.Zk_tFdOwfeUF3WH0mHpoK1dDBfjyGvjOKpUca0")

