#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 10 Jan 2017 17:35:31
#
#

import json
import sys
import re

import codecs as cc
from pymongo import MongoClient as mc

encode = 'utf-8'
pattern = re.compile(r'(\d+)\s+\w\s+(\[.*\])\s+.*')

filename = sys.argv[1]
f = cc.open(filename, 'r', encode)

mongo = mc()
db = mongo['Message']

bulk = db.msg_overdue.initialize_unordered_bulk_op()

f.readline()

for line in f.readlines():
    id, msgs_text = pattern.search(line.strip().replace('\\\\', '\\')).groups()
    msgs = json.loads(msgs_text)
    text = ' '.join(msg.get('body', ' ') for msg in msgs)

    #msg_overdue.update({"user_id": id}, {"user_id": id, "text": text}, True)
    bulk.find({"user_id": id}).upsert().update({'$set': {"text": text}})

bulk.execute()





