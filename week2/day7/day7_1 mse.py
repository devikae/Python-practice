import numpy as np
#머신러닝에 많이 쓰이는 라이브러리 백터의 연산 등 여러 도움을 줌

import matplotlib.pyplot as plt
#pip install motplotlib

data = [[2,81], [4,93], [6,91], [8,97]]
# 가상의 기울기와 y절편
fake_a_b = [3,76]

x=[i[0] for i in data]
y=[i[1] for i in data]

plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.show()

# mse 함수
def mse(y, y_hat):
    # 실제 값(y)과, 예측값(y_hat)의 차이의 제곱의 평균
    return ((y - y_hat) **2 ).mean()

# 예측 함수
def predict(x):
    return fake_a_b[0] * x + fake_a_b[1]

# mse 함수를 각 y 값에 대입하여 최종값을 구하는 함수
def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))

# 예측값이 들어갈 리스트
predict_result = []
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f , 실제 점수=%.f, 예측점수=%.f" %(x[i], y[i], predict(x[i])) )

# 최종 mse
print('mse 최종값:' + str(mse_val(predict_result, y)))