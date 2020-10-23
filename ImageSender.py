from discord.ext import commands
import os
import random
import discord
from download_helper import download as dh
import requests
from bs4 import BeautifulSoup as bs

client = commands.Bot(command_prefix="$", owner_ids=[357202840500043777, 420663223344168976])
client.remove_command('help')
random.seed(69)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Команды / bot commands: ", description= ', '.join([f'`{ctx.prefix}{command.name}`' for command in list(client.commands)]), color=0x01f912)
    embed.set_author(name="ZorgenBOT", icon_url="https://cdn.discordapp.com/attachments/767557741510131732/769002528876265472/adasdasd.jpg")
    embed.add_field(name="Бот работает только в nsfw-каналах", value="Если с ботом проблемы - пишите мне RyuK 2#9752", inline=False)
    embed.set_footer(text="INDEV v0.15")
    await ctx.send(embed=embed)
    
@client.command()
@commands.is_nsfw()
async def downgel(ctx, arg):

    if ctx.message.author.guild_permissions.administrator:
        searchTerm = arg
        url = 'https://gelbooru.me/index.php?page=dapi&s=post&q=index&tags=' + searchTerm + '&limit=100'

        rawSource = requests.get(url).content

        source = bs(rawSource, 'html.parser')

        posts = source.findAll('post')

        if not os.path.exists('delbooru'):
            os.makedirs('delbooru')
        os.chdir('delbooru')
        for post in posts:
            img_url = post['file_url']
            response = requests.get(img_url)
            if response.status_code == 200:
                embed=discord.Embed(title='Art')
                embed.set_image(url=f'attachment://image.jpg')
                response = requests.get(img_url)
                if response.status_code == 200:
                    with open('image.jpg', 'wb') as f:
                        f.write(requests.get(img_url).content)
                        f.close()

                file = discord.File(fp=os.path.abspath('image.jpg'), filename='image.jpg')

                await ctx.send(file=file, embed=embed)
                os.remove('image.jpg')

@client.command()
async def invite(ctx):
    embed=discord.Embed(title="Временно недоступно", color=0x01f912)
    embed.set_author(name="ZorgenBOT", icon_url="https://cdn.discordapp.com/attachments/767557741510131732/769002528876265472/adasdasd.jpg") 
    embed.set_footer(text="INDEV v0.15")
    await ctx.send(embed=embed)   


@client.command()
@commands.is_nsfw()
async def trap(ctx):
    images = os.listdir('./Traps')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Traps') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)


#@client.command(name='random')
#@commands.is_nsfw()
#async def _random(ctx):
#    images = os.listdir(random.choice(['Neko', 'AzurLane', 'Genshin', 'GirlsFrontline', 'Maids', 'Touhou', 'RuuyguuRena', 'Traps']))
#
#    image = images[random.randrange(len(images))]
#    file = discord.File(fp=os.path.abspath('./Random') + "\\" + image, filename='image.png')
#
#
#    embed=discord.Embed(title='Art')
#    embed.set_image(url=f'attachment://image.png')
#
#
#    await ctx.send(file=file, embed=embed)


@client.command()
@commands.is_nsfw()
async def neko(ctx):
    images = os.listdir('./Neko')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Neko') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')

    await ctx.send(file=file, embed=embed)

@client.command()
@commands.is_nsfw()
async def gachi(ctx):
    images = os.listdir('./gachi')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./gachi') + "\\" + image, filename='image.gif')


    embed=discord.Embed(title='Fisting 300 bucks')
    embed.set_image(url=f'attachment://image.gif')

    await ctx.send(file=file, embed=embed)

@client.command()
@commands.is_nsfw()
async def azurlane(ctx):
    images = os.listdir('./AzurLane')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./AzurLane') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)
 
@client.command()
@commands.is_nsfw()
async def genshin(ctx):
    images = os.listdir('./Genshin')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Genshin') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)


 
@client.command()
@commands.is_nsfw()
async def girlsfrontline(ctx):
    images = os.listdir('./GirlsFrontline')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./GirlsFrontline') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)

@client.command()
@commands.is_nsfw()
async def maid(ctx):
    images = os.listdir('./Maids')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Maids') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)

@client.command()
@commands.is_nsfw()
async def ruuyguurena(ctx):
    images = os.listdir('./RuuyguuRena')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./RuuyguuRena') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)

@client.command()
@commands.is_nsfw()
async def touhou(ctx):
    images = os.listdir('./Touhou')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Touhou') + "\\" + image, filename='image.png')


    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.png')


    await ctx.send(file=file, embed=embed)

client.load_extension('jishaku')


@commands.is_owner()
@client.command()
async def download(ctx, url = None):
    if not url: return await ctx.send('No url')


    message = await ctx.send('Started!')

    async with ctx.typing():

        task = await dh(c)

        message.edit('Done!')

    
    
    

client.run('token here')