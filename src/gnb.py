#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 03 Jan 2017 12:20:36
#
#

from config import *

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

gnb = GaussianNB()

train = np.load(train_data)
X = train[:, :-1]
y = train[:, -1]

print 'precision %f' % cross_val_score(gnb, X, y, cv=10, scoring='precision').mean()
print 'recall %f' % cross_val_score(gnb, X, y, cv=10, scoring='recall').mean()
print 'accuracy %f' % cross_val_score(gnb, X, y, cv=10, scoring='accuracy').mean()
print 'roc-auc %f' % cross_val_score(gnb, X, y, cv=10, scoring='roc_auc').mean()

