import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}





outputlist = []

def folder(folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
def get_image(page):
    url = f'https://www.123rf.com/stock-photo/dna.html?page={x}&sti=n0r30i4cahs4fsdzhv%7C'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tags = soup.find_all('img', {'class' : 'ImageThumbnail__image'})
    for tag in tags:
        title = tag.get('alt')
        href_link = tag.get('src').replace('?ver=6', '')
        dic = {
        'Title' : title,
        'URL' : href_link
    }
        outputlist.append(dic)
        print(outputlist)
        with open(href_link.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            out = requests.get(href_link)
            f.write(out.content)
            print('Downloaded..')
for x in range(1, 2):
    get_image(x)

def out_put(filename):
    df = pd.DataFrame(outputlist)
    df.to_csv('output.csv')

get_image('https://pixabay.com/images/search/rna/')
folder('images')
out_put('1.csv')





