import pandas as pd
from constants import Sentiment
from flask import jsonify

def filter_sentiment(desired_sentiment_list, sorted_df):
    return sorted_df[sorted_df['sentiment'].isin(desired_sentiment_list)]

def categorize(score: float):
    '''Categorizes score into a string Sentiment. Fine tuned values.'''
    return Sentiment.POS.value if score > 0.1 else Sentiment.ZERO.value if score > 0 else Sentiment.NEG.value

def df_to_json(dataframe):
    rows = []

    for _, row in dataframe.iterrows():
        rows.append(row.to_dict())
    
    return jsonify(rows)
