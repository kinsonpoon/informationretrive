import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

i=0
stackoverflow_url = 'https://stackoverflow.com'
df=pd.read_csv('output4300.csv')
item_title=df['Title']
item_link=df['Link']
ans=[]
for lin in item_link:
    if i%50==0:
        name='ans'+str(i)+'.csv'
        print(len(item_title[0:i]),len(ans))
        output=pd.DataFrame({'Title':item_title[0:i],'Link':item_link[0:i],'Answer':ans})
        output.to_csv(name, encoding='utf-8', index=True)   
        print(i,"converted to csv:)")
    my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' }
    target=stackoverflow_url+lin
    r = requests.get(target,  headers = my_headers)

    html = r.text # html of the webpage
    if r.status_code == requests.codes.ok:
  # parse html by BeautifulSoup
        html_soup = BeautifulSoup(html, 'html.parser')
#<div class="answercell post-layout--right">
        re=0
        try:
            for item in html_soup.find_all('div',{'class':'answercell post-layout--right'}):
                for answer in item.find_all('div',{'class':'post-text','itemprop':'text'}):
                    item_answer = item.find('p').get_text(strip=True)
                    re=1
                    ans.append(item_answer)
                    i=i+1
                    break
        #item_title.append(title)
                if re==1:
                    break
        except:
            ans.append('NA')
            i=i+1
        #print(item)
        #print(type(item))
