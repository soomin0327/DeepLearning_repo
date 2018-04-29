from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax

# Make Data sets

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0

# ont-hot encoding
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# 훈련 셋과 검증 셋 분리
x_val = x_train[42000: ]
x_train = x_train [ :42000]
y_val = y_train[42000: ]
y_test = y_test[ :42999]

# Make model
model = Sequential()
model.add(Dense(units=64, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# Setting model learning
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# learning model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_val, y_val))

# test model
loss_and_metrice = model.evaluate(x_test, y_test, batch_size=32)
print('')
print('loss_and_metrice : ' + str(loss_and_metrice))

# Use model
xhat_idx = np.random.choice(x_test, np.shape[0], 5)
xhat = x_test[xhat_idx]
yhat = model.predict_classes(xhat)

for i in range(5) :
    print('True : ' + str(argmax(y_test[xhat_idx[i]])) + 'Predict : ' + str[yhat[i]])





