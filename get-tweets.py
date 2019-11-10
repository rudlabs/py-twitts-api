#!/usr/local/bin/python3

import tweepy
from flask import Flask
from flask_restful import Resource, Api

# Variables
consumer_key = 'MRrZ7A56epXQp8ZEOeBpAwOHz'
consumer_secret = '4vh8l5ylVFriebna5AUKcMcNlwhoblC3ux8iF6WyIAG0EGWqg8'
access_token = '61522884-KoyXmgBrmG1Fn0UTO3nzjaxLxWs2ZBNBajzxVYiaa'
access_token_secret = 'sB2t1MB7kOaG2pAKLR9WXtnq8xu5r1XXH09d4rwgTOGw9'

app = Flask(__name__)
api = Api(app)

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

class GetTweet(Resource):
    def get(self):
        hashtag = '#LulaLivre'
        for tweet in tweepy.Cursor(twitter.search, q=(hashtag)).items(5):
            user = tweet.user
            return(str(user))

api.add_resource(GetTweet, '/gettweet')

if __name__ == '__main__':
    app.run(debug=True)