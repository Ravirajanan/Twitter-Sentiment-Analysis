from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from tweepy import Stream
import pandas as pd
import re

#twitter_Credentials will have the twitter api keys
import twitter_Credentials


if __name__ == '__main__':
    lis = []
    sentiment_ = []
    sentiment_name_ = []
    auth = OAuthHandler(twitter_Credentials.consumer_key, twitter_Credentials.consumer_key_secret)
    auth.set_access_token(twitter_Credentials.access_token, twitter_Credentials.acccess_token_secret)
    stop_words = set(stopwords.words('english'))

    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search, q = ['Tatamotors', 'service'], rpp= 100,lang = "en", tweet_mode = "extended"). items(1000):
        if tweet.user.screen_name != 'TataMotors_Cars':
            #print(tweet.full_text, tweet.user.screen_name)
            text = re.sub(r"@[\w]+", "", tweet.full_text)
            text = ' '.join(re.sub(r"http\S+", '', text, flags=re.MULTILINE).split())

            #tokenization
            tokens = word_tokenize(text)
            #removing stop words
            tokens_without_sw = [word for word in tokens if not word in stopwords.words()]  
            text = ' '.join(tokens_without_sw)

            analyse = TextBlob((text))
            
            
            if analyse.sentiment.polarity > 0:
                sentiment__ = 1
                sentiment_name__ = 'Good Review'
            elif analyse.sentiment.polarity == 0:
                sentiment__ = 0
                sentiment_name__ = 'Neutral'
            else:
                sentiment__ = -1
                sentiment_name__ = 'Bad Review'

            
            lis.append(text)
            sentiment_.append(sentiment__)
            sentiment_name_.append(sentiment_name__)
            
    dic = {'Tweet':lis, "Sentiment" : sentiment_, "Sentiment_name" : sentiment_name_}
    df = pd.DataFrame(dic)
    print(df.head())
    print(len(df))
    df.to_csv('tweets.csv')
    
