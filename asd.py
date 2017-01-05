# -*- coding: utf-8 -*-

import nltk
import random
import numpy as np
import pandas as pd



train_file ="/home/furkan/Masaüstü/train.csv"
train = pd.read_csv(train_file, header=None, sep=',', names = ['data','value'])





random.shuffle(train.data)

print(train.data[1])

all_words = []
for w in train.data:
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])