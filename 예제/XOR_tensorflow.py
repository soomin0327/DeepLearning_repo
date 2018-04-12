import tensorflow as tf
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])

#절단 정규분포
w = tf.Variable(tf.truncated_normal([2,2]))
b = tf.Variable(tf.zeros([2]))
h = tf.nn.sigmoid(tf.matmul(x, w) + b)

#은닉층 출력
v = tf.Variable(tf.truncated_normal([2,1]))
c = tf.Variable(tf.zeros([1]))
y = tf.nn.sigmoid(tf.matmul(h, v) +c)

#교차 엔트로피 함수
cross_entropy = -tf.reduce_sum(t * tf.log(y) + (1-t) * tf.log(1-y))

#확률 경사하강법
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for epoch in range(4000):
    sess.run(train_step, feed_dict={
        x: X,
        t: Y
    })
    if epoch % 1000 == 0:
        print("epoch: ", epoch)
        #1000번 단위로 끊어서 현재 어디인지 보여주기

classified = correct_prediction.eval(session=sess, feed_dict={
    x:X,
    t:Y
})

prob = y.eval(session=sess, feed_dict={
    x:X
})

print()
print("classified : ")
print(classified)
print()
print("out put: ")
print(prob)

#issue = 왜 1 0 1 0이 결과로 나오는 걸까..?