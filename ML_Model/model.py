'''
Trained on data from https://www.kaggle.com/uciml/news-aggregator-dataset.
Followed MSFT tutorial here: https://notebooks.azure.com/Microsoft/libraries/samples/html/Discover%20Sentiments%20in%20Tweets.ipynb
Also followed NLTK tutorial here: http://www.nltk.org/howto/sentiment.html
'''
# Other modules in project
import client

# Handling data
import pandas as pd

# Cleaning data
import re

# Miscellaneous
import os, sys

# Global variables
test_mode = True

def main(argc, argv):
    # Error checking for filename on test mode
    if test_mode and not((argc == 2) or os.path.isfile(argv[1])):
        raise IOError("Test mode requires a valid file name.")
    
    # Create DataFrame from source.
    client = Client(test_mode=test_mode)
    articles = pd.DataFrame(client.import_to_dict(filename))
    print("Shape: " + articles.shape)

def split(data):
    '''
    Splits original df into two:
    1) training_data df: data to be passed directly into model.
    2) articles df: data about a specific article that isn't useful to the model.
    Both are indexed by url.
    '''

    article_cols = ['url', 'urlToImage']
    articles = data.filter(article_cols, axis=1).set_index('url')

    training_data = data.set_index('url')
    training_data.drop('urlToImage', inplace=True)

    return (training_data, articles)

def clean(data):
    '''Cleans training DataFrame for use in model'''

    # Source id and name are redundant. Use id only.
    data.drop('name', inplace=True)

    data['author'] = extract_author(data['author'])

def extract_author(author_col):
    '''Naive way to extract author'''
    # TODO
    pass

if __name__ == '__main__':
    main(sys.argc, sys.argv)
            
