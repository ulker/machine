# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

train_file ="/home/furkan/Masaüstü/datayeni.csv"
test_file ="/home/furkan/Masaüstü/datayenitest.csv"

train = pd.read_csv(train_file, header=None, sep=',', names = ['data','value'])
test = pd.read_csv(test_file,header=None,sep=',',names=['data','value'])



text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1, 2))),
	('tfidf', TfidfTransformer(use_idf=False)),
	('clf', SGDClassifier()),
	])

text_clf = text_clf.fit(train.data, train.value)
docs_test = test.data
predicted = text_clf.predict(docs_test)
print ('% '+"%s SVM" %(text_clf.score(docs_test,test.value)*100))

text_clf1 = Pipeline([('vect1', CountVectorizer()),
	('tfidf1', TfidfTransformer(use_idf=True)),
	('clf1', MultinomialNB()),
	])
text_clf1 = text_clf1.fit(train.data, train.value)
print ('% '+"%s Naive Bayes" %(text_clf1.score(docs_test,test.value)*100))
