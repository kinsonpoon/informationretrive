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
    key=[]
    #print(tag)
    #print(query)
    '''
    for word in tag:
        if 'python' not in word:
            #print(word)
            for check in bow:
                if(str(word) in str(check)):
                    key.append(word)
                    break
    #print(key)
    try:
        search=str("+").join(key)
        print(search)
    except:
        pass
    '''
    # Target solr collection
    solr = SolrClient('http://127.0.0.1:8983/solr')

    res = solr.query('Stackoverflow', {
        "q": 'question:' + query,
        "indent": "on",
        "rows": "20",
        "wt": "json"}
    )
    '''
    try:
        tag_search = solr.query('Stackoverflow', {"q": 'tag:' + search,"indent": "on","rows": "20","wt": "json"})
        print("tagsearch")
        for i in range(3):
            print(''.join(tag_search.docs[i]['question']))
            print(''.join(tag_search.docs[i]['tag']))
    except:
        pass
    '''
    # Print the answer field of the most relevent response
    # Most relevent   = res.docs[0]
    # Second relevent = res.docs[1]
    # ...
    # And so on
    print("----------------------------------")
    print("Your Search Result")
    for i in range(3):
        print(i,''.join(res.docs[i]['question']))
    num=happy()
    while(True):
        if(num =='0'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(res.docs[0]['answer']))
            break
        elif(num =='1'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(res.docs[1]['answer']))
            break
        elif(num =='2'):
            print("----------------------------------")
            print("Here is the answer:")
            print(''.join(res.docs[2]['answer']))
            break
        else:
            print("Wrong input")
            num=happy()