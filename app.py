import tweepy
import json
from datetime import datetime
    
# Access Key and Token
consumer_key = 'MRrZ7A56epXQp8ZEOeBpAwOHz'
consumer_secret = '4vh8l5ylVFriebna5AUKcMcNlwhoblC3ux8iF6WyIAG0EGWqg8'
access_token = '61522884-KoyXmgBrmG1Fn0UTO3nzjaxLxWs2ZBNBajzxVYiaa'
access_token_secret = 'sB2t1MB7kOaG2pAKLR9WXtnq8xu5r1XXH09d4rwgTOGw9'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth, wait_on_rate_limit=True)

hashtag_list = ['#DevOps', '#APIFirst']

for hashtag in hashtag_list:
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')

    tweets_list = []

    for tweet in results:   
        user = tweet.user.name
        followers = tweet.user.followers_count
        posts = tweet.user.statuses_count
        location = tweet.user.location
        created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
        tweets_list.append({
                'HashTag': hashtag,
                'Usuario': user,
                'Seguidores': followers,
                'Posts': posts,
                'Localizacao': location,
                'Data': created})
        tweets_data = json.dumps(tweets_list)
    print (tweets_data)