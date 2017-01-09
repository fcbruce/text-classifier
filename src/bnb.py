#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 03 Jan 2017 12:20:36
#
#

from config import *

import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import cross_val_score

bnb = BernoulliNB()

train = np.load(train_data)
X = train[:, :-1]
y = train[:, -1]

print cross_val_score(bnb, X, y, cv=10, scoring='precision')
print cross_val_score(bnb, X, y, cv=10, scoring='recall')
print cross_val_score(bnb, X, y, cv=10, scoring='accuracy')
