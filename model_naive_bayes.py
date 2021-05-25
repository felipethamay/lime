# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


"""
Ler
"""
df_train = pd.read_csv('./data_train_test/df_train_imbd.csv')
df_test = pd.read_csv('./data_train_test/df_test_imbd.csv')


"""
Vetorização
"""
vect = CountVectorizer(ngram_range=(1, 1))
vect.fit(df_train.text_pt_without_stopwords)
text_vect = vect.transform(df_train.text_pt_without_stopwords)


"""
Naive Bayes
"""
model_nb = MultinomialNB()
model_nb.fit(text_vect, df_train.sentiment)