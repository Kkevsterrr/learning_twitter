#!/usr/bin/env python
from __future__ import unicode_literals
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
from TwitterSearch import *

class StdOutListener(StreamListener):

    def on_data(self, data):
        d = json.loads(data)
        retweets = d.get("retweet_count")
        #if retweets != 0 and retweets != None:
        print d.get("text")
        #print d.get("retweet_count") 
        return True

    def on_error(self, status):
        print status

def module_exists(module_name):
    '''function to check if an import exists'''
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True
def stream():
    consumer_key = 'zg9yQTGTT2oizk3XLMHGLzfpJ'
    consumer_secret = 'nmiwqRpWDX0oxTCUTro8sPeUVUXIZHW9O1VZcTb0mLyfHw51sc'
    access_token = '700001043-oxm3LZ72y4WmWGRqY66QjV0SzZoHGy5OGgwic26M'
    access_token_secret = 'hGJZWTb5bjGFSiuIQrff5UajKdlyXcp7Lyun5SJzq05Su'
    

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(locations=[-180,-90,180,90],languages = ['en'])
def pull():
    nicePrint = PrettyPrinter(indent=2, width=70)
    api = twitter.Api(consumer_key = 'zg9yQTGTT2oizk3XLMHGLzfpJ',
                      consumer_secret = 'nmiwqRpWDX0oxTCUTro8sPeUVUXIZHW9O1VZcTb0mLyfHw51sc',
                      access_token_key = '700001043-oxm3LZ72y4WmWGRqY66QjV0SzZoHGy5OGgwic26M',
                      access_token_secret = 'hGJZWTb5bjGFSiuIQrff5UajKdlyXcp7Lyun5SJzq05Su')

    #^Using twitter library we verify the app through the REST API with these keys
    
    user_info_dict = api.VerifyCredentials().AsDict()
    #^Gets my info as a dictonary

    nicePrint.pprint(user_info_dict)
    #^isplay user info
    print '\n'
       

    current_tweets = api.GetHomeTimeline()
    nicePrint.pprint([s.AsDict() for s in current_tweets])
    #^gets all current tweets in timeline(home page), and prints it all out in dicts 
def search():
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([' ']) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        ts = TwitterSearch(consumer_key = 'zg9yQTGTT2oizk3XLMHGLzfpJ',
                      consumer_secret = 'nmiwqRpWDX0oxTCUTro8sPeUVUXIZHW9O1VZcTb0mLyfHw51sc',
                      access_token = '700001043-oxm3LZ72y4WmWGRqY66QjV0SzZoHGy5OGgwic26M',
                      access_token_secret = 'hGJZWTb5bjGFSiuIQrff5UajKdlyXcp7Lyun5SJzq05Su')
        for tweet in ts.search_tweets_iterable(tso):
            #if (tweet['retweet_count'] != 0):
            print( '%s: @%s tweeted: %s' % ( tweet['retweet_count'], tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

def main():
    #pull()
    search() 
    #stream()
    


if __name__ == "__main__":
    #^This should be the first thing that is checked in the program

    #docs and stuff https://github.com/bear/python-twitter

    import collections
    import re
    from pprint import PrettyPrinter
    #^default imports that should come with python

    if not module_exists('twitter'):

        #PROMPT THE USER TO AUTO DOWNLOAD THE RIGHT PACKAGE
        print "You do not have the twitter-python module required to run this program."

        answer = raw_input("May I install it for you (Y/N)")
        while answer.lower() != 'y' or answer.lower() != 'n':#correct 'Y','N','YES','NO'
            print "I don't undestand"
            answer = raw_input("May I install it for you (Y/N)")

        if answer[0].lower() == 'y':
            print "Installing Package"
            if module_exists(pip):
                import pip
                pip.main('install','python-twitter')
            else:
                print "Pip is not installed, install pip to download packages"

    if module_exists('twitter'):
        import twitter
        main()






