#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Thu 22 Dec 2016 19:56:32
#
#

from config import *

import json
import pickle
import codecs as cc
import jieba as jb
import base64

encode = 'utf-8'

words_file = cc.open(words_path, 'r', encode)

words = {word.strip().encode(encode): [0, 0] for word in words_file.readlines()}

pos_file = cc.open(pos_parsed_train, 'r', encode)
neg_file = cc.open(neg_parsed_train, 'r', encode)

for pos in pos_file.readlines():
    ws = set(base64.b64decode(pos.strip()).split())
    for w in ws:
        w = w.strip()
        if w != '' and w in words:
            words[w][0] += 1

for neg in neg_file.readlines():
    ws = set(base64.b64decode(neg.strip()).split())
    for w in ws:
        w = w.strip()
        if w != '' and w in words:
            words[w][1] += 1

f = open(mat_path, 'wb')
pickle.dump(words, f, pickle.HIGHEST_PROTOCOL)

f.close()
pos_file.close()
neg_file.close()
words_file.close()

