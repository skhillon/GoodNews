from enum import Enum

FIREBASE_INFO = {
    "apiKey": "AIzaSyAzOV7fAcxAx7BRJuGmZgSqjtfw8eX7R30",
    "authDomain": "goodnews-58e46.firebaseapp.com",
    "databaseURL": "https://goodnews-58e46.firebaseio.com",
    "projectId": "goodnews-58e46",
    "storageBucket": "goodnews-58e46.appspot.com",
    "messagingSenderId": "767859363873"
}

class News(Enum):
    API_KEY = '88d3bf9f4bed4dfabda05fbfa5f3999e'
    BASE_URL = 'https://newsapi.org/v2/top-headlines'
    DEFAULT_PARAMS = {'country': 'us', 'category': 'general'}

class HTTP(Enum):
    '''Ensure string consistency. Add others if needed.'''
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    PUT = 'PUT'
    UNAUTHORIZED = 400

class Sentiment(Enum):
    '''Constants for sentiment classification.'''
    POS = 'positive'
    NEG = 'negative'
    ZERO = 'neutral'
