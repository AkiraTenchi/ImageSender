import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print('Message from {0.author}: {0.content}'.format(message))
    
    if message.content.startswith('$images'):
        images = os.listdir('./images')
        for image in images:
            await message.channel.send(file=discord.File(os.path.abspath('images') + "\\" + image))

client.run('Enter The Token Here')