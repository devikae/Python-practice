print('hi')

a = '안녕하세요'
print(a)

#문자열 곱하기
print(a*50)

a = '''fuck 
that 
shit'''

print(a)

#문자열 나누기(split)
b = 'life is too short'
c = b.split() #매개변수가 없으면 공백으로 자른다
print(b)
print(c)

d = "a:b:c:d"
f = d.split(':')
print(d)
print(f)

#입력 받기

#a = input('문자를 입력하세요: ')
#print(a) #변수에 입력받으면 '문자열'로 들어온다. 숫자를 입력받아도 문자열

#b = input('입력하세요: ')
#print('3+b= ', 3+int(b))

num = int(input('숫자를 입력하세요: '))
if num<10 :
    print('10보다 작음')
elif num== 100:
    print('100이다!')
else:
    print('100보다 크다')


#자료구조
# List e = [1,2 [ 'life', 'is'] ] 리스트 안에 리스트 가능 boolean 타입도 넣을수 있다.
# 인덱스로 재할당 e[1] = "True" >> 2가 "true"로 바뀜
# 인덱스자리에 음수 - 를 넣으면 뒤에서부터 접근
# 슬라이스 가능 x = a[1:3] 콜론의 위치에 따라 달라진다.
# e.append(val) e.del
# a =[1,2] b = [3,4,5] c= a+b 이런식으로 리스트 병합가능

# tuple => 리스트와 거의 동일한데 수정이 안된다.
# 리스트와 마찬가지로 슬라이스, 병합가능

# Dictionary > Java의 Map과 비슷함 key:Value 구성  ex) score={'철수':90, '민수':85 }
# 키 값으로 접근

# Set > 중복이 허용되지 않는 자료구조