import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
#Sequential은 계층 구조를 이루는 모델을 정의하는 메서드
#Dense는 구조를 이루는 창을 만드는 것

np.random.seed(0)

'''
#모델 생성 시작
'''
model = Sequential([
    Dense(input_dim=2, units=1), #입력 차원 2, 출력차원 1인 네트워크 구조를 이루는 층
    Activation('sigmoid')
])

model = Sequential()
model.add(Dense(input_dim=2, units=1))
model.add(Activation('sigmoid'))

#경사 하강법 / lr은 학습률
model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1))

'''
#모델 학습
'''
#출력 데이터 생성
X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([[0], [1], [1], [1]])

#model 실행
model.fit(X, Y, epochs=200, batch_size=1) #에폭을 200 -> 200번 실행 -> 비교

#결과 확인
classes = model.predict_classes(X, batch_size=1)
prob = model.predict_proba(X, batch_size=1)

print("classified: ")
print(classes)
print()
print("out put : ")
print(prob)