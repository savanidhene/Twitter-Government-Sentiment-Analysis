# Import Modules

import pandas as pd
import numpy as np                      
import re                                      
import string
import nltk
import warnings


warnings.filterwarnings("ignore")

# Load Datasets
def tsa():
    df = pd.read_csv('scraped_tweets.csv')
    #print(df.head())  
        # 0: Positives, 1: Negative

    #Preprocessing of Dataset

        #Remove pattern in text
    def remove_pattern(text, pattern):
        r = re.findall(pattern, text)
        for word in r:
            text=re.sub(word,"",text)
        return text

        #Remove Twitter Handles (@user)
    df['filter_tweets'] = np.vectorize(remove_pattern)(df['text'],'@[\w]*')
    #print(df.head())

        #Remove punctuation, special characters, numbers 
    df['filter_tweets'] = df['filter_tweets'].str.replace("[^a-zA-Z0-9+-]", " ")  #(^) Not Include
    #print(df.head())

    tokenized_tweets=df['filter_tweets'].apply(lambda x:x.split())
    #print(tokenized_tweets.head())

    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    tokenized_tweets=tokenized_tweets.apply(lambda sentence: [stemmer.stem(word) for word in sentence]) # lets say we have words like fight,fighting,fighter they will grp into fight
    #print(tokenized_tweets.head())

    for i in range(len(tokenized_tweets)):
        tokenized_tweets[i] = " ".join(tokenized_tweets[i]).lower()
    df['filter_tweets'] = tokenized_tweets
    #print(df.head())

    fd = pd.read_csv("positive_word.csv")
    #print(fd.head())

    def remove_pattern(text, pattern):
        r = re.findall(pattern, text)
        for word in r:
            text=re.sub(word,"",text)
        return text

        #Remove Twitter Handles (@user)

    tokenized_words=fd['Words'].apply(lambda x:x.split())
    #print(tokenized_tweets.head())

    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    tokenized_words=tokenized_words.apply(lambda sentence: [stemmer.stem(word) for word in sentence]) # lets say we have words like fight,fighting,fighter they will grp into fight

    for i in range(len(tokenized_words)):
        tokenized_words[i] = " ".join(tokenized_words[i]).lower()
    fd['filter_words'] = tokenized_words
    #print(fd.head())
    ss = tokenized_tweets.tolist()
    a=1
    aa = list()
    f = 0
    cnt=0
    count_list_positive = []
    for i in ss:
        # print("iteration:",a)
        # print(ss[f])
        aa.append(i)
        for j in aa:
            abc =j.split()
            for x in abc:
                uu = tokenized_words.tolist()
                if x in uu:
                    cnt+= 1
                    # print(x)
            count_list_positive.append(cnt)
        # print(cnt)
        aa.pop()
        cnt=0
        a+=1
        f +=1
    print(count_list_positive)

    fd = pd.read_csv("negative_word.csv")
    #print(fd.head())

    def remove_pattern(text, pattern):
        r = re.findall(pattern, text)
        for word in r:
            text=re.sub(word,"",text)
        return text

        #Remove Twitter Handles (@user)

    tokenized_words=fd['Words'].apply(lambda x:x.split())
    #print(tokenized_tweets.head())

    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    tokenized_words=tokenized_words.apply(lambda sentence: [stemmer.stem(word) for word in sentence]) # lets say we have words like fight,fighting,fighter they will grp into fight
    #print(tokenized_words.head())

    for i in range(len(tokenized_words)):
        tokenized_words[i] = " ".join(tokenized_words[i]).lower()
    fd['filter_words'] = tokenized_words

    ss = tokenized_tweets.tolist()
    a=1
    aa = list()
    f = 0
    cnt=0
    count_list_negative = []
    for i in ss:
        # print("iteration:",a)
        # print(ss[f])
        aa.append(i)
        for j in aa:
            abc =j.split()
            for x in abc:
                uu = tokenized_words.tolist()
                if x in uu:
                    cnt+= 1
                    # print(x)
            count_list_negative.append(cnt)
        # print(cnt)
        aa.pop()
        cnt=0
        a+=1
        f +=1
    print(count_list_negative)

    p = 0
    n = 1
    neu = 0
    label =[]
    i=0
    j=0
    num=1
    for num in range(200):
        # print("---------Iteration :",num)
        if count_list_positive[i] > count_list_negative[j]:
            print("positive")
            i+=1
            j+=1
            label.append(p)
        elif count_list_positive[i] < count_list_negative[j]:
            print("negative")
            i+=1
            j+=1
            label.append(n)
        else:
            print("neutral")
            i+=1
            j+=1
            label.append(neu)
    print(label)
    print("------------The End-------------")

    dp = pd.read_csv('scraped_tweets.csv')
    dp['label'] = label
    print(dp.head())
    filename = "scrapped_tweets.csv"
    dp.to_csv(filename)
    print("file saved as csv")