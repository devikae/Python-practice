import day2_9 as a
# 외부에서 호출하면 그 클래스의 내용 전부 호출이 된다.
# (import 했다는것은 파일 자체를 읽었다는것)
from  day2_9 import Rectangle as Rec # 클래스

print('cnt= ', a.Rectangle.printCnt())
print('AS Rec Cnt = ',Rec.printCnt()) # 클래스 메소드 > 객체생성 하지 않아도 클래스 임포트 시 사용 가능

a = 100
rec =Rec(a,a) # 객체 생성 (인스턴스화)
print(rec.isSquare(10,10)) #인스턴스 메소드 > 위에 객체를 생성해서 사용