# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest, chi2



train_file ="/home/furkan/Masaüstü/data.csv"

train = pd.read_csv(train_file, header=None, sep=',', names = ['data','value'])

vectorizer = CountVectorizer(lowercase=True,stop_words='english')
X = vectorizer.fit_transform(train.data)
chi2score = chi2(X,train.value)[0]

from pylab import barh,plot,yticks,show,grid,xlabel,figure
figure(figsize=(16,16))
wscores = zip(vectorizer.get_feature_names(),chi2score)
wchi2 = sorted(wscores,key=lambda x:x[0]) 
topchi2 = zip(*wchi2[-20:])
x = range(len(topchi2[1]))
labels = topchi2[0]
#print labels
'''
import csv
with open("/home/furkan/Masaüstü/kelime.csv", "w") as the_file:
    csv.register_dialect("custom", delimiter=" ", skipinitialspace=False)
    writer = csv.writer(the_file, dialect="custom")
    for tup in labels:
        writer.writerow(tup)
'''
f = open('/home/furkan/Masaüstü/kelime.txt', 'w')
for t in labels:
  f.write(''.join(str(s) for s in t) + '\n')
f.close()