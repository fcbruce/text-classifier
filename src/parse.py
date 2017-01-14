#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 19:50:21
#
#
import codecs as cc
import json
import re
import base64
import pprint as pp
from pymongo import MongoClient as mc
import ahocorasick as ac

from config import *
import jieba as jb

encode = 'utf-8'

acam = ac.Automaton()
user_dict = cc.open(user_dict_path, 'r', encode)

special_words = [word.strip().encode(encode) for word in user_dict.readlines()]

for idx, word in enumerate(special_words):
    acam.add_word(word, idx)

acam.make_automaton()

mongo = mc()
db = mongo.Message
msg_overdue = db.msg_overdue

all_words = set(special_words)

def parse_group(documents, fout=None):
    print fout
    global all_words
    for doc in documents:
        str_text = doc['text']
        words = set([special_words[item[1]] for item in acam.iter(str_text.encode(encode))])
        jb_word = set([item.encode(encode) for item in jb.cut(str_text)])

        all_words |= jb_word
        words |= jb_word

        if not words: print doc['user_id']

        plain = '\n'.join(words)
        b64_str = base64.b64encode(plain)
        fout.write(b64_str + '\n')


pos_parsed_train_file = cc.open(pos_parsed_train, 'w')
pos_parsed_test_file = cc.open(pos_parsed_test, 'w')
neg_parsed_train_file = cc.open(neg_parsed_train, 'w')
neg_parsed_test_file = cc.open(neg_parsed_test, 'w')

pos_train = msg_overdue.find({"text": {"$exists": True, '$ne': ''}, "max_overdue_days": {"$exists": True, "$gte": 3}, "creates_time": {"$lt": 1480694400}})
neg_train = msg_overdue.find({"text": {"$exists": True, '$ne': ''}, "max_overdue_days": {"$exists": True, "$lt": 3}, "creates_time": {"$lt": 1480694400}})
pos_test = msg_overdue.find({"text": {"$exists": True, '$ne': ''}, "max_overdue_days": {"$exists": True, "$gte": 3}, "creates_time": {"$gte": 1480694400}})
neg_test = msg_overdue.find({"text": {"$exists": True, '$ne': ''}, "max_overdue_days": {"$exists": True, "$lt": 3}, "creates_time": {"$gte": 1480694400}})

parse_group(pos_train, pos_parsed_train_file)
parse_group(pos_test, pos_parsed_test_file)
parse_group(neg_train, neg_parsed_train_file)
parse_group(neg_test, neg_parsed_test_file)

words_file = cc.open(words_path, 'w')
for word in all_words:
    text = word.strip()
    if text: words_file.write(text + '\n')

words_file.close()

pos_parsed_train_file.close()
pos_parsed_test_file.close()
neg_parsed_train_file.close()
neg_parsed_test_file.close()
