import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def to_csv(df,path,name,index):
    result=path+name
    df.to_csv(result, encoding='utf-8', index=True) 
path='C:\\Users\\kinsonp\\Documents\\GitHub\\informationretrive\\Dataset\\'
df=pd.read_csv(path+'ans40700.csv')
df=df.dropna()
to_csv(df,path,'data.csv',True)
bow=[]
i=0
for word in df['Tag']:
    tags=word.split()
    for tag in tags:
        if tag not in bow:
            bow.append(tag)
    i=i+1
    if(i%1000==0):
        print(i)
output=pd.DataFrame({'Bow':bow})
to_csv(output,path,'bow.csv',True)