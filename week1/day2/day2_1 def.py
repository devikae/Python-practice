# function def
# return이 없을 수도, 여러개를 return할 수도 있다.
# def calc(i, j, factor=1): factor=1 처럼 default지정가능
# 매개변수를 순서대로 넣지 않으려면 매개변수명을 써서 쓴다.
# 매개변수를 미리 알 수 없을때 가변형파라미터로 받을 수 있다
# 다른파일의 함수를 불러오려면 import day_1def as fn >> fn.calc(n,n) 이런식으로 이 클래스의 함수를 다른곳에서 임포트하고 호출 가능

# default 파라미터
def calc(i, j, factor=1):
    return i * j * factor

result = calc(10,20)
print(result)
print(calc(10,20,30))

# named 파라미터
def report(name, age, score):
    print(name, score)
report(age=10, name='kim', score='80')

# 가변길이 파라미터
def fn_total(*number):
    tot = 0
    for n in number:
        tot += n
    return tot

print(fn_total(2,3,10))
print(fn_total())

#가변길이인데 고정값이 1이 있고, 리턴을 두개 해주고싶다면?
def fn_sum_mul(flag, *args):
    count = 0
    if flag == 'sum':
        result = 0;
        for i in args:
            result +=i
            count +=1
    elif flag == 'mul':
        result = 1;
        for i in args:
            result *= i
            count += 1
    return result, count

re, cnt = fn_sum_mul('mul',2,30)
print((cnt, '번', re))



print(fn_sum_mul('sum', 3,4,5,6))
print(fn_sum_mul('mul', 3,4,5,6))