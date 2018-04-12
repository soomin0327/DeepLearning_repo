import tensorflow as tf
import numpy as np
from sklearn.utils import shuffle

#실험을 위한 변수
M = 2 #입력 데이터 차원
K = 3 #클래스 개수
n = 100 #각 클래스에 있는 데이터 수
N = n*K #전체 데이터 수

#Sample Datas
X1 = np.random.randn(n, M) + np.array([0, 10])
X2 = np.random.randn(n, M) + np.array([5,5])
X3 = np.random.randn(n, M) + np.array([10, 0])

Y1 = np.array([[1, 0, 0] for i in range(n)])
Y2 = np.array([[0, 1, 0] for i in range(n)])
Y3 = np.array([[0, 0, 1] for i in range(n)])

X = np.concatenate((X1, X2, X3), axis=0)
Y = np.concatenate((Y1, Y2, Y3), axis=0)

#모델 정의
W = tf.Variable(tf.zeros([2, 3]))
b = tf.Variable(tf.zeros([3]))

x = tf.placeholder(tf.float32, shape=[None, M])
t = tf.placeholder(tf.float32, shape=[None, K])
y = tf.nn.softmax(tf.matmul(x, W)+ b)

#교차 엔트로피 함수(미니 배치의 평균값을 계산)
#reduction_indices -> 행렬의 합을 어느 방향으로 할 것인가?
cross_entropy = tf.reduce_mean(-tf.reduce_sum(t*tf.log(y), reduction_indices=[1]))

#확률 경사 하강법
train_step = tf.train.GradientDescentOptimizer(0.1). minimize(cross_entropy)

#분류 확인
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(t,1))

#초기화
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#Model learning
batch_size = 50
n_batches = N

#에폭마다 데이터를 섞음
for epoch in range(20):
    X_, Y_ = shuffle(X, Y)

    for i in range(n_batches):
        start = i*batch_size
        end = start + batch_size

        sess.run(train_step, feed_dict={
            x: X_[start:end],
            t: Y_[start:end]
        })

X_, Y_ = shuffle(X,Y)

classified = correct_prediction.eval(session=sess, feed_dict={
    x: X_[0:10],
    t: Y_[0:10]
})

prob = y.eval(session=sess, feed_dict={
    x: X_[0:10]
})

print("classified: ")
print(classified)
print()
print("out put: ")
print(prob)

