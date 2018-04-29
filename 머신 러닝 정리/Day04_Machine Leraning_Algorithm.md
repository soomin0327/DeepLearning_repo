# 머신 러닝 기초 정리 하기

## 머신 러닝의 알고리즘 정리 해보기
3가지 : Supervised Leaning, Unsupervised Learning, Reinforcemnet Learning

# 1. Supervised Learning
Supervised Learning은 지도 학습이라고 부르는데 문제에 대한 해답이 분명하게 주어진 상태로 학습을 시키는 것 이다. <br>
= (데이터, 레이블) <br>
이 방법론으로 주로 사용 되는 구조 : CNN, RNNs <br>
ex) MNIST -> 4(28*28)이미지를 넣는다 -> 답 : 4

# 2. Unsupervised Learning
Unsupervised Learning은 비지도 학습이라고 부르며, 문제에 대한 해답이 분명하지 않을 상태로 학습을 시키는 것 이다. <br>
데이터의 숨겨져 있는 특징이나 구조를 발견하고자 할 때 쓴다. . <br>
이 방법론으로 주로 사용 되는 구조 : Autoencoders <br>
ex) Clustering : 데이터가 무작위로 분포 되어 있을 떄, 비슷한 특성 끼리 묶어서 보여주는 알고리즘

# 3. Reinforcemnet Leaning
Reinforcement Learning은 그 유명한 강화 학습이라고 부른다.<br>
강화 학습의 주 목적이라고 한 다면 주어진 환경에 대해 어떤 행동을 하면 이에 대해서 우리가 보상을 주면서 학습을 시키는 것이다.<br>
쉽게 생각하자면 [(UC Berkeley : intro to AI lec) 참조] <br>
캐릭터를 움직여 보석을 먹어야 하는 게임으로 예를 든다면, 캐릭터가 현재 보고 있는 것을 MDP라고 부른다. <br>

- MDP란?
1. Agent
캐릭터 게임을 예시로 한다면 로봇을 Agent라고 할 수 있다.<br>
그냥 현재 학습을 당하게 될 상황에 놓인 머신 러닝 모델이라고 생각하자. <br>

2. State
캐릭터가 보고 있는 현재 필드 상황이다. <br>
현재 자기가 처해 있는거나 놓여있는 상황을 인식하는 것이다.<br>
캐릭터가 보기에 "내가 지금 나무 앞에 있어." 라고 한다면 이때의 State는 "나무"가 될 것이다.<br>
그러나 만약 "내가 9번칸이고 나무 앞에 있어."라고 할 경우, State는 "9번칸, 나무" 라고 할 수도 있고, "9번칸" 또는 "나무" 라고 정의 할 수도 있다.<br>
내가 정의하고 내가 인식하기 나름이라는 뜻

3. Action



