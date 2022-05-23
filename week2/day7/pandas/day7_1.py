import pandas as pd
# 데이터프레임을 기본으로 (SQL 테이블, R의 데이터 프레임과 유사함)
# 행과 열로 이루어진 표 형태
# group by, join, 함수지원

# DB와 비슷함 인덱스있고 행과열
df= pd.DataFrame({ "name": ['Bob', 'Alex', 'Janice'], 'age': [60, 25, 33]})


print(df.head())

# 열별로 서칭 가능
df['age_plus_one'] = df['age'] +1
df['age_squared'] = df['age'] * df['age']
print(df)

total_age = df['age'].sum()
print('sum: ', total_age)

median_age = df['age'].quantitle(0.5)
print('median:', median_age)
