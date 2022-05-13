#dict key:value

score = {'철수':90, '민수':80, '영희':100}

#dict는 단순 for문 일 때 key를 반환

for key in score:
    print(key)
    print(score[key]) #키의 밸류

#dict 수정
score['철수'] = 10
#추가
score['펭수'] = 99
print(score)