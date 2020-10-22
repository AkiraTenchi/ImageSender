import discord
import os
import random

client = discord.Client()
random.seed(69)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print('Message from {0.author}: {0.content}'.format(message))

    if message.content.startswith('$help'):
        await message.channel.send("Currently available: $trap, $neko, $lolineko, $azurlane, $genshin, $girlsfrontline, $maids, $rena, $touhou")
    
    if message.content.startswith('$trap'):
        images = os.listdir('./Traps')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./Traps') + "\\" + image))
        
    if message.content.startswith('$lolineko'):
        images = os.listdir('./lolisnekos')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./lolisnekos') + "\\" + image))

    if message.content.startswith('$azurlane'):
        images = os.listdir('./AzurLane')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./AzurLane') + "\\" + image))

    if message.content.startswith('$genshin'):
        images = os.listdir('./Genshin')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./Genshin') + "\\" + image))

    if message.content.startswith('$girlsfrontline'):
        images = os.listdir('./GirlsFrontline')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./GirlsFrontline') + "\\" + image))
    
    if message.content.startswith('$maids'):
        images = os.listdir('./Maids')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./Maids') + "\\" + image))

    if message.content.startswith('$rena'):
        images = os.listdir('./RuuyguuRena')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./RuuyguuRena') + "\\" + image))

    if message.content.startswith('$touhou'):
        images = os.listdir('./Touhou')
        image = images[random.randrange(len(images))]
        await message.channel.send(file=discord.File(os.path.abspath('./Touhou') + "\\" + image))

client.run('Enter The Token Here')