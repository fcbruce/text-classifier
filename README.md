# text-classifier

使用结巴分词默认的字典分词  
计算[互信息](https://zh.wikipedia.org/wiki/%E4%BA%92%E4%BF%A1%E6%81%AF)后挑选250个词作为feature  
先使用tensorflow构造神经网络进行训练，因为数据量小加上欠采样，效果不理想  
使用xgboost，有一定的区分力  

---

训练数据中positive sample占8%  


#### TODO
加入一些人工标注的特殊单词试验  
