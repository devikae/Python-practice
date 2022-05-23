import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('./datasets/heights.csv')
x = df['height']
y = df['weight']

plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x.round())
y_data = np.array(y.round())

plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.show()
line_model = LinearRegression()
line_model.fit(x_data.reshape(-1,1), y_data)
print('공부시간 5시간으로 예측',line_model.predict([[5]]))  # 모델 예측
print(line_model.coef_)           # 기울기
print(line_model.intercept_)      # y절편
plt.plot(x_data.reshape(-1,1), y_data, 'o')
plt.plot(x_data.reshape(-1,1), line_model.predict(x_data.reshape(-1,1)))
plt.show()