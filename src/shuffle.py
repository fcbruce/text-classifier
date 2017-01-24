#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 20:30:43
#
#

import numpy as np

from config import *

pos_train = np.load(pos_mat_train_path)
pos_test = np.load(pos_mat_test_path)
neg_train = np.load(neg_mat_train_path)
neg_test = np.load(neg_mat_test_path)


train = np.vstack((pos_train, neg_train))
np.random.shuffle(train)
test = np.vstack((pos_test, neg_test))
np.random.shuffle(test)


np.save(train_data, train)
np.save(test_data, test)
