import tweepy
import time
import os
from os import environ

# Written by edmer
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
search = 'nicagajonera'

nrTweets = 500


def counter(startVal):
    num = startVal
    num += 1
    return num


keeper = True
numInd = 0
while keeper:
    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):

        numInd = numInd + counter(0)
        try:
            tweet.favorite()
            print(str(numInd) + ' ' + 'Tweet liked')
            time.sleep(8)
        except tweepy.TweepError as e:
            print(str(numInd) + ' ' + e.reason)
            time.sleep(8)