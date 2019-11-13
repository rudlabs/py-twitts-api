import tweepy
import json
from flask import Flask, jsonify
from pygelf import GelfTcpHandler, GelfUdpHandler, GelfTlsHandler, GelfHttpHandler
import logging

app = Flask(__name__)

# Access Key and Token
consumer_key = 'MRrZ7A56epXQp8ZEOeBpAwOHz'
consumer_secret = '4vh8l5ylVFriebna5AUKcMcNlwhoblC3ux8iF6WyIAG0EGWqg8'
access_token = '61522884-KoyXmgBrmG1Fn0UTO3nzjaxLxWs2ZBNBajzxVYiaa'
access_token_secret = 'sB2t1MB7kOaG2pAKLR9WXtnq8xu5r1XXH09d4rwgTOGw9'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth, wait_on_rate_limit=True)

# Raiz
@app.route('/')
def welcome():
    return jsonify({'message': 'Olá! Para obter os Tweets clique nos links de cada Hashtag',
    '#apifirst': 'http://0.0.0.0:5000/apifirst',
    '#apigateway': 'http://0.0.0.0:5000/apigateway',
    '#cloudfirst': 'http://0.0.0.0:5000/cloudfirst',
    '#devops': 'http://0.0.0.0:5000/devops',
    '#microservices': 'http://0.0.0.0:5000/microservices',
    '#oauth': 'http://0.0.0.0:5000/oauth',
    '#openapis': 'http://0.0.0.0:5000/openapis',
    '#swagger': 'http://0.0.0.0:5000/swagger',
    '#raml': 'http://0.0.0.0:5000/raml'}), 200

# /devops
@app.route('/devops')
def Get_devops():
    hashtag = "#devops"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/apifirst')
def Get_apifirst():
    hashtag = "#apifirst"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/openbaking')
def Get_openbakings():
    hashtag = "#openbaking"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200200

@app.route('/cloudfirst')
def Get_cloudfirst():
    hashtag = "#cloudfirst"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 20000

@app.route('/microservices')
def Get_microservices():
    hashtag = "#microservices"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/apigateway')
def Get_apigateway():
    hashtag = "#apigateway"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/oauth')
def Get_oauth():
    hashtag = "#oauth"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/swagger')
def Get_swagger():
    hashtag = "#swagger"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/raml')
def raml():
    hashtag = "#raml"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200

@app.route('/openapis')
def openapis():
    hashtag = "#openapis"
    results = twitter.search(
    q=(hashtag), count=100, result_type='recent')
        
    tweets_list = []
    for tweet in results:
        try:  
            user = tweet.user.name
            followers = tweet.user.followers_count
            posts = tweet.user.statuses_count
            text = tweet.text
            location = tweet.user.location
            created = tweet.created_at.strftime('%d %B %Y - %H:%M:%S')
            tweets_list.append({
                    'Hashtag': hashtag,
                    'Usuario': user,
                    'Seguidores': followers,
                    'Posts': posts,
                    'Tweet': text,
                    'Localizacao': location,
                    'Data': created})
        except:
            return {'message': 'An internal error ocurred trying to get {}'}.format(hashtag), 500
    return jsonify(tweets_list), 200
    
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.addHandler(GelfTcpHandler(host='0.0.0.0', port=12201))

if __name__ == '__main__':
    app.run(host='0.0.0.0')