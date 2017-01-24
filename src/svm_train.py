#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 30 Dec 2016 16:09:39
#
#

from sklearn import preprocessing as pp
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import numpy as np
import sklearn.metrics as skmt
import datetime
import random
import pickle as pkl

from config import *
from evaluation import calc_overdue_rate

train_mat = np.load(train_data)
test_mat = np.load(test_data)
X_train = train_mat[:, :-1]
y_train = train_mat[:, -1]
X_test = test_mat[:, :-1]
y_test = test_mat[:, -1]

scaler = pp.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#clf = SVC(C=10., kernel='rbf', gamma=3e-3, class_weight={1.: 3.95}, random_state=198964, verbose=True, cache_size=512)
clf = SVC(C=10., kernel='linear', class_weight={1.: 3.95}, random_state=2017, verbose=True, cache_size=512, probability=True)

#clf.fit(X_train, y_train)
#f = open(svm_model_path % '20170124', 'wb')
#pkl.dump(clf, f, pkl.HIGHEST_PROTOCOL)


auc = cross_val_score(clf, X_train, y_train, cv=10, scoring='roc_auc')
print auc.mean()


