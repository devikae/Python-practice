import sqlite3
conn = sqlite3.connect('stock.db')


sql = """
    INSERT INTO stocks VALUES(?, ?, ?);
"""
# INSERT INTO stocks VALUES(10001,'주석inc',1000.0); >>  이렇게 넣을 수도 있지만 매핑도 가능
# INSERT INTO stocks VALUES(?, '?', ?);  >>  Java의 Dao 만들 때 처럼 "?"를 이용해 매핑 할 수 있다
# INSERT INTO stocks VALUES(:code, :nm, :price);
cur = conn.cursor()

# cur.execute(sql) 방법1
# cur.execute(sql, '10001', '주석inc', 10000.0)  방법2
# cur.execute(sql, {'code':1001, 'nm':'주석inc', 'price':'999888'}) 방법3

#만약 여러건이 있다면

List = [
        ['1', 'A기업', 100]
        ,['2', 'B기업', 200]
        ,['3', 'C기업', 300]
]
cur.executemany(sql, List)

conn.commit()
cur.close()
conn.close()