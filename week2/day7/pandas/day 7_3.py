import pandas as pd
import cx_Oracle

# DB에서 가져오기
# 데이블의 컬럼명과 동일하게 시리즈가 나옴



conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/XE')
# df = pd.read_sql(' select * from employees', conn)
# print(df)

# salary
# df_2000 = df[['SALARY'] > 15000]
# print(df_2000)

df = pd.read_sql(""" select * 
                     from employees
                     where emp_name like '%' || :nm || '%'
                """, con=conn, params={"nm": "Steven"})
print(df)