import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}






url = 'https://www.123rf.com/stock-photo/dna.html?page=2sti=n0r30i4cahs4fsdzhv%7C'
res = requests.get(url, headers=headers)
#os.mkdir(os.path.join(os.getcwd(), folder))
#os.chdir(os.path.join(os.getcwd(), folder))
soup = BeautifulSoup(res.text, 'html.parser')
tags = soup.find_all('img', {'class' : 'ImageThumbnail__image'})
for tag in tags:
    title = tag.get('alt')
    href_link = tag.get('src').replace('?ver=6', '')
     
    with open(title.replace(' ', '_').replace('/', '') + '.jpg', 'wb') as f:
         out = requests.get(href_link)
         f.write(out.content)
         print('Downloaded..')





