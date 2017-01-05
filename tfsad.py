# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd




from sklearn.feature_extraction.text import TfidfVectorizer
train_file ="/home/furkan/Masaüstü/train.csv"
train = pd.read_csv(train_file, header=None, sep=',', names = ['data','value'])
corpus = train.data
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print dict(zip(vectorizer.get_feature_names(), idf))