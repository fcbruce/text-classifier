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
import train_util as tu

train_mat = np.load(train_data)

test_mat = np.load(test_data)

d_train = xgb.DMatrix(train_mat[:, :-1], train_mat[:, -1])
d_test = xgb.DMatrix(test_mat[:, :-1], test_mat[:,-1])

param = {
        'max_depth': 3, 
        'eta': 0.03, 
        'gamma': 1e-3, 
        'lambda': 1.1, 
        'objective': 'binary:logistic', 
        'scale_pos_weight': 11.15,
        'min_child_weight': 1.15,
        'show_stdv': False,
        'seed': random.randint(0, 65536)
        }

def auc(pred_score, d_mat):
    y_true = d_mat.get_label()
    y_pred = [float(x > 0.5) for x in pred_score]
    auc = skmt.roc_auc_score(y_true, y_pred)
    return 'auc', auc

watchlist = [(d_train, 'train'), (d_test, 'test')]
num_round = 850
bst = xgb.train(param, d_train, num_round, watchlist, feval=auc, maximize=False, verbose_eval=True)

bst.save_model(bst_model_path % str(datetime.datetime.now()))

