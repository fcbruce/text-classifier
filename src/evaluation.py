#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 06 Jan 2017 18:55:38
#
#

import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import pickle as pkl

from config import *

def calc_overdue_rate(scores, y_true, threshold):
    length = len(scores)
    total = 0
    overdue = 0
    kill = 0
    kill_count = 0
    for i in range(length):
        if scores[i] < threshold:
            total += 1.
            overdue += y_true[i]
        else:
            kill_count += 1.
            kill += y_true[i]

    overdue_rate = 0
    kill_overdue_rate = None
    pass_rate = 0

    if total > 0:
        overdue_rate = overdue / total
        pass_rate = total / length

    if kill_count > 0:
        kill_overdue_rate = kill / kill_count

    return overdue_rate, kill_overdue_rate, pass_rate

            
if __name__ == '__main__':

    model_path = sys.argv[1]

    bst = xgb.Booster(model_file=model_path)

    test_mat = np.load(test_data)
    d_test = xgb.DMatrix(test_mat)

    y_pred = bst.predict(d_test)
    y_true = test_mat[:, -1]

    print 'threshold overdue_rate pass_rate not_pass_overdue_rate'

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
        print i, overdue, pass_rate, kill_overdue

    color = [random.random(), random.random(), random.random()]
    plt.plot(ths, overdues, color=color, label='overdue_rate')
    color = [random.random(), random.random(), random.random()]
    plt.plot(ths, passes, color=color, label='pass_rate')
    color = [random.random(), random.random(), random.random()]
    plt.plot(ths, kill_overdues, color=color, label='not_pass_overdue_rate')
    plt.legend(loc='upper left')
    plt.show()
