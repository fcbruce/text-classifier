#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 17:33:00
#
#

import tensorflow as tf
import numpy as np

from config import *

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def get_train_batch(n):
    n %= 10

    res = np.load(train_data)[n * 3171: n * 3171 + 3171, :]

    return res[:, :-1], res[:, -1:]


def get_test_batch():

    res = np.load(test_data)

    return res[:, :-1], res[:, -1:]

