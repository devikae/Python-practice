# 먼저 이름과 나이를 받아라 
# 나이가 10살 미만이면 "안녕" 
# 나이가 10살에서 20살 사이면 "안녕하세요" 출력 
# 그 외 "안녕하십니까"

def sayHello(name, age):
    if 10 > age:
        print(name+": 안녕")
    elif 10 <= age and 20>= age:
        print(name+": 안녕하세요")
    else:
        print(name+": 안녕하십니까")

sayHello("ikae", 20)
sayHello("i", 9)
sayHello("kae", 40)