#!/usr/local/bin/python3

import tweepy

# Variables
consumer_key = 'MRrZ7A56epXQp8ZEOeBpAwOHz'
consumer_secret = '4vh8l5ylVFriebna5AUKcMcNlwhoblC3ux8iF6WyIAG0EGWqg8'
access_token = '61522884-KoyXmgBrmG1Fn0UTO3nzjaxLxWs2ZBNBajzxVYiaa'
access_token_secret = 'sB2t1MB7kOaG2pAKLR9WXtnq8xu5r1XXH09d4rwgTOGw9'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

def search_hashtag():
    hashtag = input('Informe uma Hashtag: ')
    for tweet in tweepy.Cursor(twitter.search, q=(hashtag)).items(100):
        user = tweet.user.screen_name
        followers = tweet.user.followers_count
        print("User: %s - Followers: %s \n" % (user, followers))
search_hashtag()