import numpy as np
#머신러닝에 많이 쓰이는 라이브러리 백터의 연산 등 여러 도움을 줌

import matplotlib.pyplot as plt
#pip install motplotlib

data = [[2,81], [4,93], [6,91], [8,97]]

x=[i[0] for i in data]
y=[i[1] for i in data]

plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.show()

# 초기 a(기울기) b(y절편)
a = 0
b = 0

# 학습률
lr = 0.05

# 몇번 학습을 진행 할지 (전체 데이터에 대해 1번씩 학습 진행을
epochs = 2001
x_data = np.array(x)
y_data = np.array(y)

# 경사하강법 GD
for i in range(epochs):
    y_hat = a * x_data + b
    error = y_data - y_hat #오차를 구하는 식

    a_diff = -(1/len(x_data)) * sum(x_data * (error)) #오차 함수를 a로 미분
    b_diff = -(1/len(x_data)) * sum(error) #오차 함수를 b로 미분

    a = a - lr * a_diff # 학습률을 곱해 a값 업데이트
    b = b - lr * b_diff # b 업데이트

    if i % 100 == 0:
        print('epoch=%.f, 기울기=%.f, y절편=%.f' %(i,a,b))

y_pred = a * x_data + b
plt.scatter(x,y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred) ])
plt.show()