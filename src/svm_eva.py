#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 30 Dec 2016 16:09:39
#
#

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

f = open(svm_model_path % '20170120', 'rb')
clf = pkl.load(f)

y_pred = clf.predict(X_test)
print skmt.roc_auc_score(y_test, y_pred)

# aucs = cross_val_score(clf, X_train, y_train, cv=10, scoring='roc_auc')
#print aucs.mean()


