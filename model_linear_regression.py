# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


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
Regressão Logistica
"""
model_lr = LogisticRegression(random_state=31)
model_lr = model_lr.fit(text_vect, df_train.sentiment)
# pred = model_lr.predict(df_test.sentiment)