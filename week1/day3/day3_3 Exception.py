# 예외

def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as e:
        print(str(e))
        print('인덱스에러')
    # except 추가
    except Exception as e:
        print(str(e))
        print('다른에러')
    else:
        print('에러없음 정상처리')
    finally:
        print('종료')

calc('시도1: ',[1,3,4])
calc('시도2: ',[1,3,])




