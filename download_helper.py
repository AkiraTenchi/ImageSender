

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from functools import partial

import discord

def generateEmbed(progess, total):
    if progres >= total:
        return discord.Embed(title='Done', color=0x01f912)
    else:
        return discord.Embed(title=f'Downloaded {progess}/total')



async def dowloadImages(url, message):
        
    # download page for parsing
    browser = webdriver.Firefox()  
    browser.get(url)  
    label = browser.find_element_by_class_name('Zr3')
    print(label)
    for i in range(0, 50):
        label.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
    html_source = browser.page_source  
    browser.quit()

    soup = bs(html_source,'html.parser')  

    # locate all elements with image tag
    image_tags = soup.findAll('img')


    print(len(image_tags))
    #print(image_tags)

    # create directory for model images
    if not os.path.exists('maids1'):
        os.makedirs('maids1')

    # move to new directory
    os.chdir('maids1')

    # image file name variable
    x = 0

    # writing images
    image_tags_amount = len(image_tags)
    for image in image_tags:
        try:
            source_set = image['srcset'].split(',')
            url = source_set[1].split(" ")[1]
            print(url)
            response = requests.get(url)
            if response.status_code == 200:
                with open('trap-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close()
                    await message.edit(embed=generateEmbed(x, image_tags_amount))
                    x += 1

           

          
        except:
            pass

async def download(bot, url, ctx):
    await bot.loop.create_task(dowloadImages(url=url, message=ctx))
