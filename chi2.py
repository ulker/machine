# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest, chi2



train_file ="/home/furkan/Masaüstü/train.csv"
test_file ="/home/furkan/Masaüstü/test.csv"

train = pd.read_csv(train_file, header=None, sep=',', names = ['data','value'])
test = pd.read_csv(test_file,header=None,sep=',',names=['data','value'])

vectorizer = CountVectorizer(lowercase=True,stop_words='english')
X = vectorizer.fit_transform(train.data)
chi2score = chi2(X,train.value)[0]

from pylab import barh,plot,yticks,show,grid,xlabel,figure
figure(figsize=(16,16))
wscores = zip(vectorizer.get_feature_names(),chi2score)
wchi2 = sorted(wscores,key=lambda x:x[1]) 
topchi2 = zip(*wchi2[-25:])
x = range(len(topchi2[1]))
labels = topchi2[0]
print labels
barh(x,topchi2[1],align='center',alpha=.2,color='g')
plot(topchi2[1],x,'-o',markersize=5,alpha=.8,color='g')
yticks(x,labels)
xlabel('$\chi^2$')
show()
