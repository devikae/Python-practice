import pandas as pd
#데이터 프레임의 1열은 시리즈 구조

s = pd.Series([1, 2, 3])
print(s)

print(s + 1)

# 시리즈 끼리 연산 가능
print(s + pd.Series([ 2, 3, 4])) # 길이가 같은 시리즈를 더하면 성분 별로 덧셈


# 조인
df_w_age = pd.DataFrame({"name":['Tom','Tyrell','Claire']
                         ,"age":[60, 25, 33]})

df_w_height = pd.DataFrame({"name":['Tom','Tyrell','Claire']
                         ,"height":[6.2, 4.0, 5.5]})

# 공통적으로 name이 들어있고 값이 같음
# "name" 기준으로 join
joined = df_w_age.set_index("name").join(df_w_height.set_index('name'))
print(joined)
print(joined.reset_index())

df = joined.reset_index()
# 함수지원
# def agg(p_df):
#     return pd.Series({"name":max(p_df['name'])
#                       ,"oldset": max(p_df['age'])
#                       ,"mean_height": p_df['heiget'].mean()})
#
# print(df.apply(agg))

# lambda 지원함 익명함수 (휘발성)
re = (lambda x: x+1)(3)  #

print('정의와 동시에 사용', re)
print((lambda x, y: x+y)(10,20))
# 객체에 담아 사용
func = lambda x,y : x * y + 1
print(func(4, 2))

df['age_squar'] = df['age'].apply(lambda x: x * x)
print(df)

func1 = lambda x: x * x
df['age_squar2'] = df['age'].apply(func1)
print(df)