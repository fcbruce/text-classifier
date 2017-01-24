#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 10 Jan 2017 19:06:16
#
#

from pymongo import MongoClient as mc

import sys
import re
import datetime
import time

filename = sys.argv[1]

f = open(filename, 'r')

f.readline()

mongo = mc()
db = mongo.Message
bulk = db.msg_overdue.initialize_unordered_bulk_op()

for line in f.readlines():
    user_id, loan_account_id, max_overdue_days, isnull, creates_time = line.strip().split()

    creates_time = int(time.mktime(datetime.datetime.strptime(creates_time, "%Y-%m-%d").timetuple()))
    max_overdue_days = int(max_overdue_days)
    bulk.find({"user_id": user_id}).upsert().update({"$set": {"loan_account_id": loan_account_id, "max_overdue_days": max_overdue_days, "creates_time": creates_time}})

bulk.execute()

f.close()
