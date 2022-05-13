import os
# os같은 경우 local시스템에 접근할때 필요한 lib 현재경로나, 파일의위치 찾을 때 많이 사용

print(os.getcwd()) # 현재위치
fileNm = 'delay.txt'
fileNm = 'bot.py'
if os.path.exists(fileNm): # 해당파일이 존재 하는지 boolean
    if os.path.isfile(fileNm): #파일이라면?
        os.remove(fileNm) #파일삭제
    if os.path.isdir(fileNm): #디렉토리라면?
        os.rmdir(fileNm)
    print('삭제되었습니다. ')

# 파일지울땐 isfile 디렉토리는 isdir
