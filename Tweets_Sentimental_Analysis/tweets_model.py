import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns                          # For making stats graphics
import re                                      # To get particular phrase
import string
import nltk
import warnings
warnings.filterwarnings("ignore")

def analyze():
    df = pd.read_csv('scrapped_tweets.csv')
    #print(df.head())  

    def remove_pattern(text, pattern):
        r = re.findall(pattern, text)
        for word in r:
            text=re.sub(word,"",text)
        return text

        #Remove Twitter Handles (@user)
    df['filter_tweet'] = np.vectorize(remove_pattern)(df['hashtags'],'@[\w]*')
    #print(df.head())

    df['filter_tweet'] = df['filter_tweet'].str.replace("[^a-zA-Z#]", " ")  #(^) Not Include
    #print(df.head())


        #Remove short words 
    df['filter_tweet'] = df['filter_tweet'].apply(lambda x: " ".join([w for w in x.split() if len(w) >3]))  # if word len > 3 it will add it to str or ignore
    #print(df.head())

    tokenized_tweets=df['filter_tweet'].apply(lambda x:x.split())
    #print(tokenized_tweets.head())

        #stem the words
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    tokenized_tweets=tokenized_tweets.apply(lambda sentence: [stemmer.stem(word) for word in sentence]) # lets say we have words like fight,fighting,fighter they will grp into fight
    #print(tokenized_tweets.head())

    #combine the words into single sentence
    for i in range(len(tokenized_tweets)):
        tokenized_tweets[i] = " ".join(tokenized_tweets[i])
    df['filter_tweet'] = tokenized_tweets
    #print(df.head())

    #Exploratory Data Analysis
        # Display Frequent +ve Words
    all_words =" ".join([sentence for sentence in df['filter_tweet'][df['label']==1]]) #join all +ve words in single variable
    from wordcloud import WordCloud
    wordcloud = WordCloud(width=800, height=500,random_state=42,max_font_size=100).generate(all_words)
    '''
        #plot the graph 
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    '''
        # Display Frequent -ve Words
    all_words =" ".join([sentence for sentence in df['filter_tweet'][df['label']==0]]) #join all -ve words in single variable
    from wordcloud import WordCloud
    wordcloud = WordCloud(width=800, height=500,random_state=42,max_font_size=100).generate(all_words)
        #plot the graph 
    '''
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #plt.show()
    '''
        #Extract the (#)
    def hashtag(tweets):
        hashtags = []
            #loop words in the tweet
        for tweet in tweets:
            ht = re.findall(r"#(\w+)",tweet)
            hashtags.append(ht)
        return hashtags

        #Extract #s from +ve and -ve tweets      
    ht_positive = hashtag(df['filter_tweet'][df['label']==1])
    ht_positive = sum(ht_positive,[])  #combine into single list
    ht_negative = hashtag(df['filter_tweet'][df['label']==0])
    ht_negative = sum(ht_negative,[]) #combine into single list



        #for +ve tweets
    freq = nltk.FreqDist(ht_positive)
    d = pd.DataFrame({'Hashtag':list(freq.keys()),'Count':list(freq.values())})
    #print(d.head())

        #Select top 10 Hashtags
    d =d.nlargest(columns='Count',n=10)
    #plt.figure(figsize=(15,9))
    #sns.barplot(data=d,x='Hashtag',y='Count')
    #plt.show()

    freq = nltk.FreqDist(ht_negative)
    d = pd.DataFrame({'Hashtag':list(freq.keys()),'Count':list(freq.values())})
    #print(d.head())

        #Select top 10 Hashtags
    d =d.nlargest(columns='Count',n=10)
    '''
    plt.figure(figsize=(15,9))
    sns.barplot(data=d,x='Hashtag',y='Count')
    plt.show()
    '''

    #Input Split
        #Feature Extract
    from sklearn.feature_extraction.text import CountVectorizer #no of occurences of the words
    bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2,max_features=1000,stop_words='english')
    bow =bow_vectorizer.fit_transform(df['filter_tweet'])

        #Training & Testing datasets
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test= train_test_split(bow,df['label'], random_state=42, test_size=0.25)

    #Model Training
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import f1_score, accuracy_score

        #Training
    model = LogisticRegression()
    model.fit(x_train, y_train)

        #Testing
    pred = model.predict(x_test)
    z = f1_score(y_test,pred)
    acc = accuracy_score(y_test,pred)
    print(z)
    print(acc)

        #Use probability to get output
    pred_prob = model.predict_proba(x_test)
    pred = pred_prob[:,1] >= 0.3
    pred = pred.astype(np.int)
    z = f1_score(y_test,pred)
    acc = accuracy_score(y_test,pred)
    print(z)
    print(acc)
    
