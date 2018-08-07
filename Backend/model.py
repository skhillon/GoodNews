from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import util

def rank_article_positivity(articles_dict):
    '''Runs article json through model using 'title' field. Returns sorted DataFrame.'''
    # Import article objects into DataFrame for easier use.
    ranked_by_compound = pd.DataFrame(articles_dict)
    scores = []
    analyzer = SIA()

    for article in ranked_by_compound['title']:
        score_dict = analyzer.polarity_scores(article)
        scores.append(score_dict['compound'])

    ranked_by_compound['compound'] = scores
    ranked_by_compound['sentiment'] = ranked_by_compound['compound'].apply(util.categorize)
    
    ranked_by_compound.sort_values('compound', ascending=False, inplace=True)
    ranked_by_compound.reset_index(drop=True, inplace=True)

    return ranked_by_compound
