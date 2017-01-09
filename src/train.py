#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 17:22:20
#
#

import sklearn.metrics as skmt
import tensorflow as tf
import numpy as np
import datetime

from config import *
import train_util as tu

seed = 0

x = tf.placeholder(tf.float32, shape=[None, vec_length])
y_ = tf.placeholder(tf.float32, shape=[None, 1])

W1 = tu.weight_variable([vec_length, 100])
b1 = tu.weight_variable([100])
y1 = tf.matmul(x, W1) + b1
h1 = tf.nn.relu(y1)
keep_prob = tf.placeholder(tf.float32)
h1_drop = tf.nn.dropout(h1, keep_prob)

W_fc = tu.weight_variable([100, 1])
b_fc = tu.weight_variable([1])
y_nn = tf.matmul(h1_drop, W_fc) + b_fc

loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(y_nn, y_))
train_step = tf.train.AdadeltaOptimizer(1e-3).minimize(loss)

y_sig = tf.sigmoid(y_nn)
pred = tf.greater(y_sig, 0.5)
correct_pred = tf.equal(tf.cast(pred, tf.float32), y_)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

saver = tf.train.Saver()

for i in range(0, 100001):
    train_batch = tu.get_train_batch(i)
    if i % 50 == 0:
        y_true = train_batch[1]
        acc = accuracy.eval(feed_dict={
            x: train_batch[0], y_: train_batch[1], keep_prob: 1.0})
        los = loss.eval(feed_dict={
            x: train_batch[0], y_: train_batch[1], keep_prob: 1.0})
        y_pred = pred.eval(feed_dict={
            x: train_batch[0], keep_prob: 1.0})
        recall = skmt.recall_score(y_true, y_pred)
        precision = skmt.precision_score(y_true, y_pred)
        f1 = skmt.f1_score(y_true, y_pred)
        print "step #%d: train accuracy %f, loss %f" % (i, acc, los)
        print "          recall %f, precision %f, f1 %f" % (recall, precision, f1)
    if i % 100 == 0:
        test_batch = tu.get_test_batch()
        y_true = test_batch[1]
        acc = accuracy.eval(feed_dict={
            x: test_batch[0], y_: test_batch[1], keep_prob: 1.0})
        y_pred = pred.eval(feed_dict={
            x: test_batch[0], keep_prob: 1.0})
        recall = skmt.recall_score(y_true, y_pred)
        precision = skmt.precision_score(y_true, y_pred)
        f1 = skmt.f1_score(y_true, y_pred)
        print "step #%d: test accuracy %f" % (i, acc)
        print "          recall %f, precision %f, f1 %f" % (recall, precision, f1)

    train_step.run(feed_dict={x: train_batch[0], y_: train_batch[1], keep_prob: 0.5})

    if i > 0 and i % 10000 == 0:
        path = saver.save(sess, tf_model_path % (str(datetime.datetime.now()) + '-' + str(i)))
        print path

