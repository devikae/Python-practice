# 입력 받은 수 만큼
# 로또 번호 생성 해주세요
import random

mylotto = set()

count = int(input('몇개나만들까요?: '))

for i in range(count) :
    mylotto.clear()

    while len(mylotto) < 6:
        rotto = random.randint(1, 45)
        mylotto.add(rotto)

    print(mylotto)






