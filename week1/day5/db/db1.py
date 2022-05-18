import sqlite3
import os
path = os.getcwd()+'/db/'
# conn = sqlite3.connect(':memory:') # 일회성

conn = sqlite3.connect(path+'stock.db')
# 해당위치에 파일로 생성, 있으면 접속

print(sqlite3.version)

cur = conn.cursor()
#커서 객체

cur.execute("""
    CREATE TABLE stocks(st_code varchar2(10)
                        ,st_nm   varchar2(10)
                        ,st_price number)

""")
cur.close()
conn.close()