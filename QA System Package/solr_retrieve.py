from SolrClient import SolrClient
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def happy():
    print("----------------------------------")
    print("Type the number that you would like to take a closer look")
    number= input("Number:")
    return number
    print("----------------------------------")
def just4fun():
    print("----------------------------------")
    print("It is a simple retrieval-based QA system about python and data is come from stackoverflow")
    print("Just type in ur question abt python in full sentecnce")
    print("Type \"exit\" if u want to exit")
    print("Happy searching")
    print("----------------------------------")
df=pd.read_csv('.\Dataset\\bow.csv')
bow=df['Bow']
#print(bow[0])
while True:
    just4fun()
    query = input("Query: ")
    if(query =='exit'):
        break
    # Preprocessing
    # The query should be "How+do+you+do"
    # Instead of "How do you do"
    tag=query.split(" ")
    query = query.replace(" ", "+")
    key={}
    #print(tag)
    #print(query)
    
    for word in tag:
        key[word]=1
        if 'python' not in word:
            #print(word)
            for check in bow:
                if(str(word) == str(check)):
                    #print(str(check))
                    key[word]=2
                    break
        
            
    #print(key)
    # Target solr collection
    solr = SolrClient('http://127.0.0.1:8983/solr')

    res = solr.query('Stackoverflow', {
        "q": 'question:' + query,
        "indent": "on",
        "rows": "20",
        "wt": "json"}
    )
    print("----------------------------------")
    print("Your Search Result")
    score={}
    top=[]
    for i in range(10):
        #print(i,''.join(res.docs[i]['question']))
        score[str(res.docs[i]['question'])]=0
        for word in key:
            #print(word)
            if (word in str(res.docs[i]['question'])):
                score[str(res.docs[i]['question'])]+=key[word]
        #print(score[str(res.docs[i]['question'])])
    #print(sorted(score.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
    for i in range(5):
        top.append(sorted(score.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)[i])
    result=[]
    #print(top)
    for element in top:
        for pairs in res.docs:
           # print(pairs['question'])
           # print(element[0])
            if(str(pairs['question'])==str(element[0])):
                result.append(pairs)
                break
    #print(result)
    for i in range(3):
        print(i,''.join(result[i]['question']))
        #print(i,''.join(res.docs[i]['question']))
        #print(''.join(res.docs[1]['tag']))
    
    num=happy()
    while(True):
        if(num =='0'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(result[0]['answer']))
            break
        elif(num =='1'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(result[1]['answer']))
            #print(''.join(res.docs[1]['tag']))
            break
        elif(num =='2'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(result[2]['answer']))
            #print(''.join(res.docs[1]['tag']))
            break
        else:
            print("Wrong input")
            print("----------------------------------")
            for i in range(3):
                print(i,''.join(result[i]['question']))
            num=happy()
    