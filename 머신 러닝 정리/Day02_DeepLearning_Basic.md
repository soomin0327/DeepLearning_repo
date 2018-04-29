# Basic_Deep Learning

## 훈련, 검증, 시험 셋
1. 어떠한 결과를 실제로 얻기 위해서 모델에 대한 평가를 기반으로 나눈 데이터들의 분류라고 생각하자

2. 훈련 셋 : 모델의 학습을 위해서 넣어주는 여러가지 데이터들 
<br>(ex> 고양이 사진을 100장 다른걸 넣는다)

3. 검증 셋 : 학습된 것을 가지고 반복적인 동작을 통해 테스트와 수정을 거치는데에 사용되는 데이터 (성능 검사)
<br>(ex> 강아지 사진 -> true -> 수정)
<br>(ex> 고양이 사진 -> true -> 유지)
4. 시험 셋 : 실제로 데이터를 넣고 비교
5. 다음은 실전에 투입

## 기본 단어
실제 적용 : (모델 학습 : model.fit(x, y, batch_size=32, epochs = 100))

1. batch_size : 몇 개를 써서 할껀가
    - 사이즈가 작으면 작을 수록 가중치 갱신이 자주 일어남
2. epochs :몇 번을 반복할껀가
3. loss : 매 epochs 마다의 손실값
4. ass : " 정확도
5. val_loss : " 검증 손실값
5. val_acc : " 검증 정확도

## 기본 예제
- MNIST
- Block Question -> Make -> Test
- CNN Model
- GAN Model
- LSTM Model