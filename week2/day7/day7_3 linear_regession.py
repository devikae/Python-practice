import numpy as np
#머신러닝에 많이 쓰이는 라이브러리 백터의 연산 등 여러 도움을 줌
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#pip install sklearn 머신러닝 알고리즘 지원 lib

data = [[2,81], [4,93], [6,91], [8,97]]

x=[i[0] for i in data]
y=[i[1] for i in data]

plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

line_model = LinearRegression()
print(x_data)
print(x_data.reshape(-1,1))
line_model.fit(x_data.reshape(-1,1), y_data)


print('공부시간 5시간으로 에측: ',line_model.predict([[5]])) # 모델 예측
print('기울기:', line_model.coef_) # 기울기
print('y절:', line_model.intercept_) # y절편
plt.plot(x_data.reshape(-1,1), y_data, 'o')
plt.plot(x_data.reshape(-1,1), line_model.predict(x_data.reshape(-1,1)))

plt.show()
