import pysolr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('output4300.csv')
link=df['Link']
title=df['Title']
QA_Pair_list = []
i=0
while(True):
    try:
        QA_Pair = {}
        QA_Pair['id'] = i
        QA_Pair['question'] = title[i]
        QA_Pair['answer'] = link[i]
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
solr = pysolr.Solr('http://127.0.0.1:8983/solr/helloworld', timeout=60)

# Import all data in QA_Pair_list
solr.add(QA_Pair_list)
