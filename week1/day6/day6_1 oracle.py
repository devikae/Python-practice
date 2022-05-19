import cx_Oracle
#pip install cx_Oracle

def fn_search(name):

    conn = cx_Oracle.connect('study','study','localhost:1521/XE')
    print(conn.version)

    memberList = []

    #with를 쓰게되면 따로 close를 해주지 않아도 된다
    with conn:
        cur =conn.cursor()
        sql='''
            select mem_name
                 , mem_id
                 , mem_mail
                 , mem_job
                 , mem_mileage
            from member
            where mem_name like '%' || :word || '%' 
        '''

        # search = input("검색어 입력: ")
        # print(search)
        rows = cur.execute(sql, {'word':name})
        # de = rows.description
        # colums = [d[0] for d in rows.description]

        for i in rows:
            memberList.append(i)

    # print(memberList)
    return memberList

# 터미널에서 고객 이름을 입력받아
# 아이디, 이메일, 직업, 마일리지를 리턴

nm = input("이름 입력: ")
print(fn_search(nm))



