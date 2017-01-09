#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 06 Jan 2017 11:20:19
#
#

import matplotlib.pyplot as plt
import numpy as np
import sys
import re
import random

fname = sys.argv[1]

l_p = re.compile(r'\[(\d+?)\]\s+train-\w+:(\d*.*\d*?)\+*\d*.*\d*\s+test-\w+:(\d*.*\d*?)\+*\d*.*\d*')

train = []
test = []
iters = []

f = open(fname, 'r')
for line in f.readlines():
    res = l_p.search(line)
    if res: 
        iter, train_value, test_value = res.groups()
        iters.append(int(iter))
        train.append(float(train_value))
        test.append(float(test_value))

color = [random.random(), random.random(), random.random()]
plt.plot(iters, train, color=color, label='train')
color = [random.random(), random.random(), random.random()]
plt.plot(iters, test, color=color, label='test')
plt.legend(loc='lower right')
plt.show()

f.close()
