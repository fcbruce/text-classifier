#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 03 Jan 2017 11:50:37
#
#

from config import *

import numpy as np

pos = np.load(pos_mat_path)
neg = np.load(neg_mat_path)

train =  np.vstack((pos[: train_pos_count, :], neg[: train_neg_count, :]))
test =  np.vstack((pos[-test_pos_count: , :], neg[-test_neg_count: , :]))

np.random.shuffle(train)
np.random.shuffle(test)

np.save(train_data, train)
np.save(test_data, test)
