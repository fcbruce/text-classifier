#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 26 Dec 2016 15:55:52
#
#

from config import *

import numpy as np
import codecs as cc
import json
import base64

encode = 'utf-8'

pos_train = cc.open(pos_parsed_train, 'r', encode)
pos_test = cc.open(pos_parsed_test, 'r', encode)
neg_train = cc.open(neg_parsed_train, 'r', encode)
neg_test = cc.open(neg_parsed_test, 'r', encode)

token = cc.open(token_path, 'r', encode)

tokens = {}

token_id = 0
for line in token:
    word = line.strip().split(',')[0]
    tokens.setdefault(word, token_id)
    token_id += 1

def build_mat(count, file, label):
    mat = np.zeros((count, vec_length + 1), dtype=np.float32)
    mat[:, -1] = label

    id = 0
    for line in file.readlines():
        text = base64.b64decode(line).decode(encode).split()
        for word in text:
            word = word.strip()
            if tokens.has_key(word):
                mat[id][tokens[word]] += 1
        id += 1

    return mat

pos_mat_train = build_mat(train_pos_count, pos_train, 1.)
neg_mat_train = build_mat(train_neg_count, neg_train, 0.)
pos_mat_test = build_mat(test_pos_count, pos_test, 1.)
neg_mat_test = build_mat(test_neg_count, neg_test, 0.)

np.save(pos_mat_train_path, pos_mat_train)
np.save(pos_mat_test_path, pos_mat_test)
np.save(neg_mat_train_path, neg_mat_train)
np.save(neg_mat_test_path, neg_mat_test)

pos_train.close()
pos_test.close()
neg_train.close()
neg_test.close()
