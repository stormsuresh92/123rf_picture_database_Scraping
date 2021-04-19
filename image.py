import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}

output list = []


url = 'https://www.123rf.com/stock-photo/dna.html?page=2sti=n0r30i4cahs4fsdzhv%7C'
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
       

df = pd.DataFrame(outputlist)
df.to_csv('output.csv')
print('file downloaded.')





