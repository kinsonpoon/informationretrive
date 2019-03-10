import requests
from bs4 import BeautifulSoup
import os.path
import numpy as np
import scipy as spy
import pandas as pd
item_title=[]
item_link=[]
for i in range(1,10000):
    
# access html by Requests
    stackoverflow_url = 'https://stackoverflow.com/questions/tagged/python?' # stackoverflow URL
    my_params = {'sort':'votes','page':str(i)} # parameter
    my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' }

# download stackoverflow result
    r = requests.get(stackoverflow_url, params = my_params, headers = my_headers)

    html = r.text # html of the webpage

    if r.status_code == requests.codes.ok:
  # parse html by BeautifulSoup
        html_soup = BeautifulSoup(html, 'html.parser')

        for item in html_soup.find_all('div',{'class':'summary'}):
            item_a = item.find('a')
            link = item_a.get('href')
            title = item.find('h3').get_text(strip=True)
            item_title.append(title)
            item_link.append(link)
#print("Title:", item_title)
    if(i%100==0):
        name='output'+str(i)+'.csv'
        output=pd.DataFrame({'Title':item_title,'Link':item_link})
        output.to_csv(name, encoding='utf-8', index=True)   
        print(i,"converted to csv:)")
#print("Link:", item_link, "\n")

        
