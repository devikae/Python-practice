# set > 중복이 안된다
from builtins import enumerate

myset = {1,3,4,6,1}

test={} # << 이건 dictionary로 인식
print(type(test))

myset2 =set()
print(type(myset2)) #type() 안에 넣으면 자료형을 알 수 있다.

print(myset) # 1, 3, 4, 6 이 나온다

# 요소 추가
myset2.add(10)
# 여러 요소 한번에 추가
myset2.update({4,9,99,10,110,100})
for i, v in enumerate(myset2):
    print(i, '번째', v)

# 하나만 삭제
myset2.remove(9)
print(myset2)
# 모든 요소 삭제
myset2.clear()
print(myset2)

