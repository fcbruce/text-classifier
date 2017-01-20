#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 30 Dec 2016 16:09:39
#
#

import xgboost as xgb
import numpy as np
import sklearn.metrics as skmt
import datetime
import random

from config import *
from evaluation import calc_overdue_rate

mat = np.load(train_data)

def get_kth_train_test(k):
    n, m = mat.shape
    patch_size = n / 10
    begin = patch_size * k
    end = (k == 9 and n) or (begin + patch_size)
    test_mat = mat[begin: end, :]
    train_mat = mat[end:, :] if k == 0 else mat[: begin, :] if k == 9 else np.vstack((mat[: begin, :], mat[end: , :]))
    d_train = xgb.DMatrix(train_mat[:, :-1], train_mat[:, -1])
    d_test = xgb.DMatrix(test_mat[:, :-1], test_mat[:, -1])

    return d_train, d_test

param = {
        'max_depth': 2, 
        'eta': 0.01, 
        'gamma': 0.5, 
        'lambda': 0.3, 
        'objective': 'binary:logistic', 
        'scale_pos_weight': 3.95,
        'min_child_weight': 2.15,
        'subsample': 0.5,
        'colsample_bytree': 0.5,
        #'max_delta_step': 1,
        'show_stdv': False,
        'seed': random.randint(0, 65536)
        }

def auc(pred_score, d_mat):
    y_true = d_mat.get_label()
    y_pred = [float(x > 0.5) for x in pred_score]
    auc = skmt.roc_auc_score(y_true, y_pred)
    return 'auc', auc


for k in range(10):
    d_train, d_test = get_kth_train_test(k)
    watchlist = [(d_train, 'train'), (d_test, 'test')]
    num_round = 3600

    #cv = xgb.cv(param, d_train, num_round, feval=auc, maximize=False, verbose_eval=True, show_stdv=False)

    bst = xgb.train(param, d_train, num_round, watchlist, feval=auc, maximize=False, verbose_eval=True)

    bst.save_model((bst_model_path % str(datetime.datetime.now())) + str(k))

