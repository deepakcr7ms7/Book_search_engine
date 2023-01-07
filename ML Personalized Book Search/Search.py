import pandas as pd
from IPython.display import display
title=pd.read_json('books_titles.json')

#to make search easier we conver titles into TF-IDF score

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizor=TfidfVectorizer()

tfidf=vectorizor.fit_transform(title['mod_title'])

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

#query_search_

query='The Hunger Games'
user_id=2

def mark_click(val):
    return '<img src="{}" width=50></img>'.format(val)

#process the qurey as we did with ours titles
def search_query(query,vectorizor):

    processed_query=re.sub('[^a-zA-Z0-9]','',query.lower())
    #get the TFidf score
    score=vectorizor.transform([processed_query])
    #search-using cosine transfrom

    similarity=cosine_similarity(score,tfidf).flatten()
    # similarity is cosine score of all tiltes and current query

    #now to get the 10 highest values of cosine similarity

    indices=np.argpartition(similarity,-10)[-10:]

    #result we will get the actual titles

    result=title.iloc[indices]
    #print(result)

    #search_result
    result=result.sort_values('ratings',ascending=False)
    #result_collabrartive_filtering
    top_recs=pd.read_csv('top_recs.csv')
    top_recs.drop(['mod_title', 'mean','count','adjusted_count','score'], axis=1, inplace=True)
    result.drop(['mod_title'], axis=1, inplace=True)
    pd.concat([top_recs,result])
    #result = result.merge(top_recs, how="inner", on="book_id")

    return result.head(5).style.format({'cover_image':mark_click})


df=search_query(query, vectorizor)
df.render()
display(df)