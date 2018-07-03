import requests, json

class Client:
    __API_KEY = '88d3bf9f4bed4dfabda05fbfa5f3999e'
    __BASE_URL = 'https://newsapi.org/v2/top-headlines'
    __default_params = {'country': 'us', 'category': 'general'}

    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def import_to_dict(self, filename=None, params=self.__default_params):
        '''Imports data as dict. If test_mode, uses local file. Otherwise uses api'''
        raw_json = None

        if self.test_mode:
            with open(filename) as f:
                return json.load(f)       
        else:
            return self.__get_raw_json(params)

    def __get_raw_json(self, **kwargs):
        payload = kwargs
        payload['apiKey'] = __API_KEY
        return requests.get(__BASE_URL, params=payload).raise_for_status().json()
