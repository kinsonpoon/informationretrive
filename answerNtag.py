import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def get_tag(html_soup):
    tag=""
    try:
        for item in html_soup.find_all('div',{'class':"grid ps-relative d-block"}):
            tag=(item.text)
        #item_title.append(title)
    except:
        #ans.append('NA')
        tag='NA'
        #print(item)
        #print(type(item))
    return tag

def get_answer(html_soup):
    #print("start")
    re=0
    item_answer=""
    try:
        for item in html_soup.find_all('div',{'class':'answercell post-layout--right'}):
            for answer in item.find_all('div',{'class':'post-text','itemprop':'text'}):
                item_answer+=answer.text
        #item_title.append(title)
            re=1
            break
    except:
        #ans.append('NA')
        re=1
        item_answer='NA'
        #print(item)
        #print(type(item))
    return item_answer

stackoverflow_url = 'https://stackoverflow.com'
df=pd.read_csv('output4300.csv')
item_title=df['Title']
item_link=df['Link']
ans=[]
tag=[]
for lin in item_link:
    if len(ans)%50==0:
        path='C:\\Users\\kinsonp\\Documents\\GitHub\\informationretrive\\Dataset\\'
        name=path+'ans'+str(len(ans))+'.csv'
        print(len(item_title[0:len(ans)]),len(ans))
        output=pd.DataFrame({'Title':item_title[0:len(ans)],'Link':item_link[0:len(ans)],'Answer':ans,'Tag':tag})
        output.to_csv(name, encoding='utf-8', index=True)   
        print(len(ans),"converted to csv:)")
    my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' }
    target=stackoverflow_url+lin
    r = requests.get(target,  headers = my_headers)

    html = r.text # html of the webpage
    if r.status_code == requests.codes.ok:
  # parse html by BeautifulSoup
        html_soup = BeautifulSoup(html, 'html.parser')
#<div class="answercell post-layout--right">
        ans.append(get_answer(html_soup))
        #print(ans[0].splitlines())
        tag.append(get_tag(html_soup))