from pymongo import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

client = MongoClient('localhost',27017)
db = client.twitterdb

col = db.tweets

keywords = ['Fenimismo', 'LGBTQ','Pronome Neutro','Social']

consumer_key = "jkDwioRJQprLfWCHbocBCa1qu"
consumer_secret = "f4glvA8gdn6cfQKJiNfVD9Frdu3RghwubNDUu8rFGulCOfSzYZ"
access_token = "1269412466842308610-1zOq8qBwxFoIw5hnlmDydyOxzGwy2h"
access_token_secret = "luYHZqQlYUPElL6unYPJLUQyGyMJ06GlUKbpTgI6xDhvE"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyListener(StreamListener):
    
    def on_data(self,dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at, "id_str":id_str,"text":text,}
        col.insert_one(obj)
        print(obj)
        return True

def exec():
    mylistener = MyListener()
    mystream = Stream(auth,listener = mylistener)
    mystream.filter(track=keywords)
    mystream.disconnect()

def tweetsMongo():
    dataset = [{"created_at":item["created_at"], "text": item["text"],} for item in col.find()]
    df = pd.DataFrame(dataset)
    print(df) 
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df.text)

    word_count = pd.DataFrame(cv.get_feature_names(), columns=['word'])
    word_count['count'] = count_matrix.sum(axis=0).tolist()[0]
    word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
    print(word_count[:50])
  
   

tweetsMongo()