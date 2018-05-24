# Liner Regression 이론

1. Regression<br>
데이타 셋을 통해 학습을 하면 범위로 값을 내보낸다.<br>
ex> 시험 시간과 점수 데이터(traning data)를 기반으로 물어보면 대답해준다. <br>

2. Linear Regression 기초<br>
데이터 셋 x: 1,2,3 | y: 1,2,3<br>
이것을 그래프로 나타낸다면 Linear Hypothesis(가설)을 만들 수 있다.<br>
즉, 우리가 가지고 있는 데이터가 어느 선에 맞을까? -> 학습하는 것이다.<br>
<br>
수학적 정리 : H(x) = Wx+b<br>
선의 모양은 W와 b에 영향을 받는다.<br>

> 어느 선이 가장 적합한 선일까??

3. Linear Regression<br>
 > H(x) = Wx+b

- Cost function(loss function): 데이터와 가설의 값이 얼마나 차이가 있는가?(차를 구하는 것이다)<br>
-> (H)x)-y*y) = cost function<br>
데이터 각각에 대한 값들을 각각 계산 하는 과정을 미적으로 나타내게 되면, 수식이 나온다.<br>
-> Linear Regression의 최종 목표 : minimize cost(W,b)하는 W와 b를 구하는 것


