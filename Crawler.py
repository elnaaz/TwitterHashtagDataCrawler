# -*- coding: utf-8 -*- from __future__ import unicode_literals
import tweepy, webbrowser
from twython import Twython
from Storage import *
from AccessKeyGenerator import *


#main file
class Crawler:
    def searchTweetsByHashtag(self, hashtag):
        #you can generate this values by AccessKeyGenerator class
        TWITTER_ACCESS_TOKEN = ''
        TWITTER_ACCESS_TOKEN_SECRET = ''

        auth = tweepy.OAuthHandler(AccessKeyGenerator.CONSUMER_KEY, AccessKeyGenerator.CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        storage = Storage()

        for tweet in tweepy.Cursor(api.search, q=hashtag, count=1000, result_type="recent").items():
            storage.save(tweet)


crawler = Crawler()
#Example - get tweets by #sms2014 hashtag
crawler.searchTweetsByHashtag('#sms2014')
