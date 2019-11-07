#!/usr/bin/python2.7

# Importing modules
import sys
import tweepy

# Variables
consumer_key = 'MRrZ7A56epXQp8ZEOeBpAwOHz'
consumer_secret = '4vh8l5ylVFriebna5AUKcMcNlwhoblC3ux8iF6WyIAG0EGWqg8'
access_token = '61522884-KoyXmgBrmG1Fn0UTO3nzjaxLxWs2ZBNBajzxVYiaa'
access_token_secret = 'sB2t1MB7kOaG2pAKLR9WXtnq8xu5r1XXH09d4rwgTOGw9'
word = sys.argv[1]

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

# Searching twitters
results = twitter.search(q="%s" % (word))
for tweet in results:
    user = tweet.user.screen_name
    followers = tweet.user.followers_count
    message = tweet.text
    print("User: %s - Followers: %s - Tweet: %s" % (user, followers, message))
