import pysolr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('.\dataset\data.csv')
title=df['Title']
answer=df['Answer']
tags=df['Tag']
QA_Pair_list = []
i=0
ignor='python'


while(True):
    try:
        QA_Pair = {}
        QA_Pair['id'] = i
        QA_Pair['question'] = title[i]
        QA_Pair['answer'] = answer[i]
        tag=tags[i].split()
        key=[]
        for t in tag:
            if(ignor not in t):
                key.append(t)
        key=str(" ").join(key)
        QA_Pair['tag']=key
        QA_Pair_list.append(QA_Pair)
        i=i+1
    except:
        break

# KEY represents the field of the target collection
# VALUE represents the value of the corresponding field
# QA_Pair[KEY] = VALUE

'''
QA_Pair = {}
QA_Pair['id'] = 0
QA_Pair['question'] = 'Hi, how do you do?'
QA_Pair['answer'] = 'I feel good ~'
QA_Pair_list.append(QA_Pair)

QA_Pair = {}
QA_Pair['id'] = 1
QA_Pair['question'] = 'Nice to meet you!'
QA_Pair['answer'] = 'Nice to meet you too'
QA_Pair_list.append(QA_Pair)
'''

# Define the target solr collection
solr = pysolr.Solr('http://127.0.0.1:8983/solr/Stackoverflow', timeout=60)

# Import all data in QA_Pair_list
solr.add(QA_Pair_list)
print("import finished")