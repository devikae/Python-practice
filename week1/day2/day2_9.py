class Rectangle:
    count = 0 # 클래스의 필드변수

    #init 메소드
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 인스턴스 메소드
    def calcArea(self):
        area = self.width * self.height
        return  area

    # 정적 메소드
    @staticmethod
    def isSquare(width, height):
        print('정적 메소드')
        return width == height

    # 클래스 메소드
    # 갹체를 만들지 않아도 클래스이름으로 호출 가능
    @classmethod
    def printCnt(cls):
        print(cls.count)
        cls.count += 1
        return cls.count

if __name__== '__main__':
    print('main')
    # 인스턴스 생성
    a = 20
    myRec = Rectangle(a,a)

    #인스턴스 메소드는 인스턴스가 있어야 사용가능
    print(myRec.calcArea())

    # 정적 메소드는 self, class 없이 사용 가능
    print(Rectangle.isSquare(a,a))

# 다른곳에서 import 했을 때
else:
    print('another module')