from multiprocessing.pool import ThreadPool
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import os


class DownloadImages:
    def __init__(self):
        self.errors = 0

    def download_url(self, data):
        referer = data.split(' ')[0]
        url = data.split(' ')[1]
        filename = os.path.abspath('./images') + '/' + unquote(url.split('/')[-1])
        try:
            response = requests.get(url, headers={'referer': referer})
            with open(filename, "wb") as out:
                out.write(response.content)
            print(f'Completed Image ====>', filename)
        except:
            self.errors += 1


def scrape_links(url):
    """Scraping links to media(images and gifs) & post link to them"""
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    post_links = ['http://fapreactor.com' + post_link_body.attrs['href'] for post_link_body in soup.findAll('a', class_='link')]
    media_links = []
    for post_link in tqdm(post_links, desc="Scraping links", bar_format="{l_bar}{bar}| {elapsed}<{remaining}"):
        response = requests.get(post_link)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        for soup_media_link in soup.findAll('div', class_ = 'image'):
            try:
                media_links.append(f"{post_link} {soup_media_link.find('a').attrs['href']}")
            except AttributeError:
                pass

    return media_links


def fapreactor_download(url):
    url = url if url.startswith('http://') else ('http://' + quote(url))
    media_links = scrape_links(url)
    print('Starting downloading')
    downloader = DownloadImages()
    results =  ThreadPool(5).imap_unordered(downloader.download_url, media_links)
    for i in results:
        pass
