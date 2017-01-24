#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 19:56:48
#
#
import sys
import os

# 3rd party
sys.path.append('../lib/3rd/jieba')

data_dir = '../data'
model_dir = '../model'

pos_raw = os.path.join(data_dir, 'positive_raw.data')
pos_json = os.path.join(data_dir, 'positive.data')
pos_parsed_train = os.path.join(data_dir, 'positive_parsed_train.data')
pos_parsed_test = os.path.join(data_dir, 'positive_parsed_test.data')
pos_mat_train_path = os.path.join(data_dir, 'positive_mat_train.npy')
pos_mat_test_path = os.path.join(data_dir, 'positive_mat_test.npy')
neg_raw = os.path.join(data_dir, 'negative_raw.data')
neg_json = os.path.join(data_dir, 'negative.data')
neg_parsed_train = os.path.join(data_dir, 'negative_parsed_train.data')
neg_parsed_test = os.path.join(data_dir, 'negative_parsed_test.data')
neg_mat_train_path = os.path.join(data_dir, 'negative_mat_train.npy')
neg_mat_test_path = os.path.join(data_dir, 'negative_mat_test.npy')

words_path = os.path.join(data_dir, 'words.data')
mat_path = os.path.join(data_dir, 'mat.data')
mi_path = os.path.join(data_dir, 'mi.data')

train_data = os.path.join(data_dir, 'train.data.400.npy')
test_data = os.path.join(data_dir, 'test.data.400.npy')
train_data_500 = os.path.join(data_dir, 'train.data.500.npy')
test_data_500 = os.path.join(data_dir, 'test.data.500.npy')

user_dict_path = os.path.join(data_dir, 'dict_extern.txt')
def_dict_path = os.path.join('../lib/3rd/jieba/jieba', 'dict.txt')

token_path = os.path.join(data_dir, 'select_token_20170111.data')

tf_model_path = os.path.join(model_dir, 'tf/%s.ckpt')
bst_model_path = os.path.join(model_dir, 'xgb/%s.model')
svm_model_path = os.path.join(model_dir, 'svm/%s.model')

pos_count = 11049
neg_count = 43681
vec_length = 400

test_pos_count = 763
test_neg_count = 2983

train_pos_count = pos_count - test_pos_count
train_neg_count = neg_count - test_neg_count

total_count = pos_count + neg_count
