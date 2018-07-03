from api_model import HTTP, Sentiment
from flask import Flask, jsonify, request
import tensorflow as tf
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def hello():
    '''Used as a sanity check.'''
    return 'API is up and running!'

@app.route('/predict', methods=[HTTP.POST.value])
def predict():
    '''Main prediction method, calls several helper functions. Returns JSON to caller.'''
    if request.method != HTTP.POST.value:
        return jsonify(method=request.method, error='This route requires a POST request.')
    try:
        # TODO
        # article = request.get_json()
        # score, sentiment, error = calculate_sentiment(article)
        # return jsonify(score=score, sentiment=sentiment, error=error)

        return jsonify(score=0.1, sentiment=Sentiment.POS.value, error='Generic')
    except ValueError:
        return jsonify(error='Please supply a valid Article object as JSON.')
    except Exception as e:
        return jsonify(error=e)

def calculate_sentiment(article):
    '''
    Runs the article dict through a model to provide sentiment analysis score.

    Negative: -1 to 0
    Neutral: 0
    Positive: 0 to 1
    '''
    score = None
    graph, error = load_model('recommendation-model')

    if error:
        return None, None, error

    try:
        y_pred = graph.get_tensor_by_name("y_pred:0")
        x = graph.get_tensor_by_name("x:0")

        with tf.Session(graph=graph) as sess:
            feed_dict_testing = {x: article} # TODO: fix
            score = sess.run(y_pred, feed_dict=feed_dict_testing)
    except Exception as e:
        error = e

    sentiment = categorize(score)
    return score, sentiment, error


def load_model(name: str):
    '''
    Loads frozen model and variables from disk.

    name - path without file extensions.
    '''
    path = './{}.pb'.format(name)
    error = None

    try:
        with tf.gfile.GFile(path, "rb") as f:
            restored_graph_def = tf.GraphDef()
            restored_graph_def.ParseFromString(f.read())

        with tf.Graph().as_default() as graph:
            tf.import_graph_def(
                restored_graph_def,
                input_map=None,
                return_elements=None,
                name=""
            )
    except Exception as e:
        error = e
    
    return graph, error

def categorize(score: int):
    '''Categorizes score into a string Sentiment.'''
    if (score == 0):
        return Sentiment.ZERO
    else:
        return Sentiment.POS if score > 0 else Sentiment.NEG

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8000"), debug=True)