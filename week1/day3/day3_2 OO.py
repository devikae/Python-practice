# 연산자 오버로딩
class NumBox:
    def __init__(self, num):
        self.num = num
    def __add__(self, others):
        print('다른 객체', others.num)
        self.num += others.num
    def __sub__(self, num):
        self.num -+ num

# 연산자를 객체에 사용
n = NumBox(10)
n2 = NumBox(100)
n + n2
print(n.num)
