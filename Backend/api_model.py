from enum import Enum

class HTTP(Enum):
    '''Ensure string consistency. Add others if needed.'''
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    PUT = 'PUT'

class Sentiment(Enum):
    '''Constants for sentiment classification.'''
    POS = 'positive'
    NEG = 'negative'
    ZERO = 'neutral'