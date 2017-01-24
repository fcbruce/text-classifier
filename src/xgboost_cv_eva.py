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
import matplotlib.pyplot as plt

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


all_ths = []
all_overdues = []
all_kill_overdues = []
all_passes = []

models = ['2017-01-17 15:05:04.886357.model0', '2017-01-17 15:15:44.734819.model1',
        '2017-01-17 15:26:21.773331.model2', '2017-01-17 15:37:10.043410.model3',
        '2017-01-17 15:47:43.879654.model4', '2017-01-17 15:58:42.759957.model5',
        '2017-01-17 16:09:35.508684.model6', '2017-01-17 16:20:26.826395.model7',
        '2017-01-17 16:30:54.947887.model8', '2017-01-17 16:41:22.374055.model9']

for k in range(10):
    d_train, d_test = get_kth_train_test(k)

    bst = xgb.Booster(model_file=('../model/xgb/' + models[k]))

    y_pred = bst.predict(d_test)
    y_true = d_test.get_label()
    print y_true

    ths = []
    overdues = []
    kill_overdues = []
    passes = []
    for i in np.arange(0, 1.01, 0.01):
        ths.append(i)
        overdue, kill_overdue, pass_rate = calc_overdue_rate(y_pred, y_true, i)
        overdues.append(overdue)
        kill_overdues.append(kill_overdue)
        passes.append(pass_rate)

    all_ths.append(ths)
    all_overdues.append(overdues)
    all_kill_overdues.append(kill_overdues)
    all_passes.append(passes)

    #cv = xgb.cv(param, d_train, num_round, feval=auc, maximize=False, verbose_eval=True, show_stdv=False)

    #bst = xgb.train(param, d_train, num_round, watchlist, feval=auc, maximize=False, verbose_eval=True)

    #bst.save_model((bst_model_path % str(datetime.datetime.now())) + str(k))

ths = np.average(all_ths, axis=0)
overdues = np.average(all_overdues, axis=0)
kill_overdues = np.average(all_kill_overdues, axis=0)
passes = np.average(all_passes, axis=0)
print 'threshold overdue_rate pass_rate not_pass_overdue_rate'
for i in range(101):
    print ths[i], overdues[i], passes[i], kill_overdues[i]

color = [random.random(), random.random(), random.random()]
plt.plot(ths, overdues, color=color, label='overdue_rate')
color = [random.random(), random.random(), random.random()]
plt.plot(ths, passes, color=color, label='pass_rate')
color = [random.random(), random.random(), random.random()]
plt.plot(ths, kill_overdues, color=color, label='not_pass_overdue_rate')
plt.legend(loc='upper left')
plt.show()
