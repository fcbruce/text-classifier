# text-classifier


2016/12/05之前有数据： 
```
db.msg_overdue.count({text: {$exists: true, $ne: ''}, max_overdue_days: {$exists: true, $gt: 2}})
db.msg_overdue.count({text: {$exists: true, $ne: ''}, max_overdue_days: {$exists: true, $lt: 3}})
```
pos: 11049  
neg: 43681  
rate: 0.20188196601498265

------

12/03 - 12/05: 用作测试
```
db.msg_overdue.count({text: {$exists: true, $ne: ''}, max_overdue_days: {$exists: true, $gt: 2}, creates_time: {$gte: 1480694400}})
db.msg_overdue.count({text: {$exists: true, $ne: ''}, max_overdue_days: {$exists: true, $lt: 3}, creates_time: {$gte: 1480694400}})
```
pos: 763  
neg: 2983  
rate: 0.20368392952482647  

### 算法策略
先用special word hit，然后jieba分词，算互信息，然后train
