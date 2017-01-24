#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 11 Jan 2017 17:18:52
#
#

from pymongo import MongoClient as mc
import json
import codecs as cc
import sys
import re

pattern = re.compile(r'(\d+)\s+(\[.*\])')

encode = 'utf-8'

filename = sys.argv[1]
f = cc.open(filename, 'r', encode)

mongo = mc()
db = mongo.Message
bulk = db.msg_overdue.initialize_unordered_bulk_op()

f.readline()

count = 0

for line in f.readlines():
    matched = pattern.search(line.strip().replace('\\\\', '\\'))
    if matched:
        loan_account_id, msgs_text = matched.groups()
        msgs = json.loads(msgs_text)
        text = ' '.join(msg.get('body', ' ') for msg in msgs)

        bulk.find({"loan_account_id": loan_account_id}).update({'$set': {"text": text}})

bulk.execute()



f.close()
