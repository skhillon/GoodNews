import requests

API_KEY = '88d3bf9f4bed4dfabda05fbfa5f3999e'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def get_raw_json(**kwargs):
    payload = kwargs
    payload['apiKey'] = API_KEY
    return requests.get(BASE_URL, params=payload).raise_for_status().json()
