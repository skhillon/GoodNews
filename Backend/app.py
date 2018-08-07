# Project-specific modules
import model
import auth
import client
import util
from constants import HTTP, Sentiment, FIREBASE_INFO

# External modules
import pyrebase
# `request` and `jsonify` are for client -> backend.
from flask import Flask, jsonify, request
# `requests` and `json` are for backend -> external.
import requests
import json

app = Flask(__name__)

firebase = pyrebase.initialize_app(FIREBASE_INFO)

@app.route('/', methods=[HTTP.GET.value])
def getNews():
    raw_articles = client.get_raw_articles(test_mode=False, test_filename='Backend/top-headlines.json')
    ranked = model.rank_article_positivity(raw_articles)

    # No negative news!
    good_articles = util.filter_sentiment([Sentiment.POS.value, Sentiment.ZERO.value], ranked)

    return util.df_to_json(good_articles)

@app.route('/test')
def test():
    '''Used as a sanity check.'''
    return 'API is up and running!'

@app.route('/login/<route>', methods=[HTTP.POST.value])
def login(route):
    '''Logs in a user. For now only uses email and password, assumes user already exists. Returns user idToken.'''
    # TODO: Figure out which button pressed. For now always assume email login.
    if route == 'email':
        return auth.login_with_email(firebase)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
