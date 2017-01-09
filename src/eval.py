#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 06 Jan 2017 18:55:38
#
#

import xgboost as xgb
import numpy as np
import sys

from config import *

def calc_overdue_rate(scores, y_true, threshold):
    length = len(scores)
    total = 0
    overdue = 0
    for i in range(length):
        if scores[i] < threshold:
            total += 1.
            overdue += y_true[i]

    if total < 1: return 0, 0
    return overdue / total, total / length
            


model_path = sys.argv[1]

bst = xgb.Booster(model_file=model_path)

test_mat = np.load(test_data)

d_test = xgb.DMatrix(test_mat[:, :-1], test_mat[:, -1])

y_pred = bst.predict(d_test)
y_true = test_mat[:, -1]

print 'threshold, overdue rate, pass rate'

for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    print i, calc_overdue_rate(y_pred, y_true, i)

