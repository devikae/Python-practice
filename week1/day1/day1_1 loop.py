# 동적배열 List
a = []
b = [1, 2, 3]
c = [1, 2, 'list', 'is']
d= [1,2, [3, 4]]

# 리스트 인덱스 -1: 마지막요소
#            -2: 뒤에서 두번째
# 중첩리스트 d[2][0] <- d의 3번째 요소의 0번째 요소

print(c[-1])
print(d[2][0])

# 슬라이스
# [처음인덱스: 마지막인덱스+1]
print(d[1:3])
f = ['This', 'is', 'a', 'book', 'is']
print(f.count('is')) # 요소에서 값을 찾아 카운트
print(d*10)

# 반복문 - for

# 해당 리스트에서 하나씩 밸류값이 i에 온다 > 값 자체가 필요할 때
arr = ['one', 'two', 'three']
for i in arr:
    print(i)

# index, value 모두 필요할 때
for i, v in enumerate(arr): #i에 index v에 value
    print(i, '번째', v)

# 단순 반복
for i in range(1, 5): # 5번 실행하는데 시작점을 1로 정해줄 수 있음 ragne(n) > n 만큼 반복 range(x,n) x번부터 n번까지 반복
    print(i, end=' ') # end=' ' 를 넣어주게 되면 한줄로 나열해서 출력할 수 있음


#question
#입력받은 수 만큼 hi를 출력하시오
print()
#a = int(input('숫자를 입력하세요: '))

#for i in range(a):
#    print('hi')

import random
num = random.randint(1,10) #1~10 사이 정수값 반환
print(num)

# 반복문 - while

chance = int(input('몇번만에 맞출수있냐? 입력: '))
if chance > 10:
    print('10번이상은 양심 없지 기회는 최대 5번')
    chance = 5
elif chance < 5:
    chance = chance

while chance > 0:
    user_num = int(input('1~10 임의의 수를 맞춰보세요! 입력: '))
    if num == user_num:
        print('맞췄다 정답은:', num)
        break
    else:
        chance = chance - 1
        print('틀렸다 남은기회: ', chance)

        if num > user_num:
            print('up')
        elif num < user_num:
            print('down')