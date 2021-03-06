import json
import requests
import copy
from constants import News

def get_raw_articles(test_mode=False, test_filename=None):
    '''Queries appropriate news source and returns json object. Must specify test_filename if test_mode=True.'''
    if test_mode:
        with open(test_filename) as f:
            return json.load(f)['articles']
    else:
        params = copy.deepcopy(News.DEFAULT_PARAMS.value)
        params['apiKey'] = News.API_KEY.value
        return _query_news_api(params)
        
def _query_news_api(params):
    raw_json = requests.get(News.BASE_URL.value, params=params).json()
    return raw_json['articles']

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response