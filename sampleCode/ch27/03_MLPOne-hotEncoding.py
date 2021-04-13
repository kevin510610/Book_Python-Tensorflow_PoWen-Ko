#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import tensorflow as tf
import numpy as np


x1=np.random.random((500,1))
x2=np.random.random((500,1))+1
x_train=np.concatenate((x1, x2))

y1=np.zeros((500,), dtype=int)
y2=np.ones((500,), dtype=int)
y_train=np.concatenate((y1, y2))


# 將數字轉為 One-hot 向量
y_train2 = tf.contrib.keras.utils.to_categorical(y_train,  num_classes=2)

# 建立模型
model = tf.contrib.keras.models.Sequential()
model.add(tf.contrib.keras.layers.Dense(units=10,
    activation=tf.nn.relu,
    input_dim=1))
model.add(tf.contrib.keras.layers.Dense(units=10,
    activation=tf.nn.relu ))  # tf.nn.relu
model.add(tf.contrib.keras.layers.Dense(units=2,
    activation=tf.nn.softmax ))  #tf.nn.softmax

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(optimizer='adam',
    loss=tf.contrib.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])

"""
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
"""

model.fit(x_train, y_train2,
          epochs=20,
          batch_size=128)



#測試
x_test=np.array([[0.22],[0.31],[1.22],[1.33]])
y_test=np.array([0,0,1,1])
y_test2 = tf.contrib.keras.utils.to_categorical(y_test,  num_classes=2)

score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("predict:",predict)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])


