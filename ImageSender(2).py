from discord.ext import commands
import os
import random
import discord
from download_helper import download as dh
import requests
from bs4 import BeautifulSoup as bs
from new_fp_parser import fapreactor_download

client = commands.Bot(command_prefix="$", owner_ids=[357202840500043777, 420663223344168976])
client.remove_command('help')
random.seed(69)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def help(ctx):
    embed=discord.Embed(title="**Доступные команды:**", color=0xff0000)
    embed.set_author(name="Art_maid BOT", icon_url="https://cdn.discordapp.com/attachments/719220249165037639/769241273390465045/adasdasd.jpg")
    embed.add_field(name="$arts", value="Доступные арты", inline=False)
    embed.add_field(name="$invite", value="Как добавить бота на свой сервер", inline=False)
    embed.add_field(name="$gachi", value="???", inline=False)
    embed.set_footer(text="INDEV v0.25")
    await ctx.send(embed=embed)

@client.command()
async def adminhelp(ctx):
    if ctx.message.author.guild_permissions.administrator:
        embed=discord.Embed(title="**Команды для админов:**", color=0xff0000)
        embed.set_author(name="Art_maid BOT", icon_url="https://cdn.discordapp.com/attachments/719220249165037639/769241273390465045/adasdasd.jpg")
        embed.add_field(name="$gelbooru <tag> <amount>", value="Загрузка артов с gelbooru по тегу. Максимум 100 изображений.", inline=False)
        embed.set_footer(text="INDEV v0.25")
        await ctx.send(embed=embed) 

@client.command()
async def arts(ctx):
    embed=discord.Embed(title="**Доступные арты:**", color=0xff0000)
    embed.set_author(name="Art_maidBOT", icon_url="https://cdn.discordapp.com/attachments/719220249165037639/769241273390465045/adasdasd.jpg")
    embed.add_field(name="$maid", value="Горничные", inline=False)
    embed.add_field(name="$ruuyguurena", value="Когда плачут цикады / Рюгу Рена", inline=False)
    embed.add_field(name="$azurlane", value="Azur Lane", inline=False)
    embed.add_field(name="$genshin", value="Genshin Impact", inline=False)
    embed.add_field(name="$trap", value="Ловушки", inline=False)
    embed.add_field(name="$neko", value="Неко-неко няя~", inline=False)
    embed.add_field(name="$loli", value="на 8 лет поедем? :)", inline=False)
    embed.add_field(name="$touhou", value="Touhou Project", inline=False)
    embed.add_field(name="$girlsfrontline", value="Герои аниме Girls Frontline", inline=False)
    embed.set_footer(text="INDEV v0.25")
    await ctx.send(embed=embed)   
    
@client.command()
@commands.is_nsfw()
async def fapreactor(ctx, arg):
    os.mkdir('images')
    fapreactor_download('http://fapreactor.com/tag/' + arg)
    embed=discord.Embed(title='Art')
    embed.set_image(url=f'attachment://image.jpg')
    for img in os.listdir('./images'):
        file = discord.File(fp='./images/' + img, filename='image.jpg')
        await ctx.send(file=file, embed=embed)
    os.rmdir('./images')

@client.command()
@commands.is_nsfw()
async def gelbooru(ctx, arg, amn):

    if ctx.message.author.guild_permissions.administrator:
        searchTerm = arg
        amountDownload = amn
        url = 'https://gelbooru.me/index.php?page=dapi&s=post&q=index&tags=' + searchTerm + '&limit=' + amountDownload

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
    embed=discord.Embed(title="**Ссылка для приглашения бота:**", description="[**Пригласить бота на свой сервер**](https://discord.com/oauth2/authorize?client_id=768940182752854056&scope=bot&permissions=67618880)", color=0xff0000)
    embed.set_author(name="Art_maidBOT", icon_url="https://cdn.discordapp.com/attachments/719220249165037639/769241273390465045/adasdasd.jpg")
    embed.add_field(name="Бот работает только в NSFW-каналах", value="Если бот тупит / не отвечает - RyuK 2#9752", inline=True)
    embed.set_footer(text="INDEV v0.25")
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

@client.command()
@commands.is_nsfw()
async def loli(ctx):
    images = os.listdir('./Neko')
    image = images[random.randrange(len(images))]
    file = discord.File(fp=os.path.abspath('./Neko') + "\\" + image, filename='image.png')


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
@commands.is_nsfw()
async def downgel(ctx, arg, amn):

    searchTerm = arg
    amountDownload = amn

    embed=discord.Embed(title="Скачиваю тег " + searchTerm + " " + amountDownload , color=0xff0000)
    embed.set_author(name="Art_maidBOT", icon_url="https://cdn.discordapp.com/attachments/719220249165037639/769241273390465045/adasdasd.jpg")
    embed.set_footer(text="INDEV v0.25")
    await ctx.send(embed=embed)

    url = 'https://gelbooru.me/index.php?page=dapi&s=post&q=index&tags=' + searchTerm + '&limit=' + amountDownload

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

#@commands.is_owner()
#@client.command()
#async def download(ctx, url = None):
#    if not url: return await ctx.send('No url')
#
#
#    message = await ctx.send('Started!')
#
#    async with ctx.typing():
#
#        task = await dh(c)
#
#        message.edit('Done!')

    
    
    

client.run('NzY4OTQwMTgyNzUyODU0MDU2.X5HxWQ.ikMgtNuJlpq0chDSomTa-nWjeYY')
#client.run('NzY5MjIzODgwOTUwMDIyMTQ0.X5L5kA.Bb1sHtF08mLtaBQk3KcM46MTIHE')