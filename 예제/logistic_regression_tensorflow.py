import tensorflow as tf
import numpy as np


#랜덤 시드 설정
tf.set_random_seed(0)

#모델 정의
#w랑 b 설정하기
w = tf.Variable(tf.zeros([2,1]))
b = tf.Variable(tf.zeros([1]))

#x,t,y 설정하기
#None은 마음대로 설정 할 수 있도록 하는 가변 설정이다
x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])
y = tf.nn.sigmoid(tf.matmul(x, w)+b) #sigmoid function [H(x) * w +b]

#교차 엔트로피 오차 함수
#tf.reduce_sum()은 np.sum()과 같다
cross_entropy = -tf.reduce_sum(t * tf.log(y) + (1-t) * tf.log(1-y))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
#경사하강법 -> 오차는 0.1

correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)),t)

'''
#학습시작
'''

#OR 게이트
X = np.array([[0,0], [0,1], [1,0], [1,1]]) #OR 게이트의 동작을 보기 위해서 배열 삽입
Y = np.array([[0], [1], [1], [1]]) #비교 할 배열

#초기화
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#학습
for epoch in range(200):
    sess.run(train_step, feed_dict={
        x: X,
        t: Y
    })

'''
#결과 도출
'''

#eval은 적절하게 맞게 분류했는지에 대한 여부를 보여주는 것
classified = correct_prediction.eval(session=sess, feed_dict={
    x: X,
    t: Y
})

prob = y.eval(session=sess, feed_dict={
    x: X
})

print("classified : ")
print(classified)
print()
print("output : ")
print(prob)

