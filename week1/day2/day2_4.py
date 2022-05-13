import os

root = os.getcwd()
searchNm = input('찾고 싶은 파일명: ')
# 해당 위치의 파일 정보 가져오기
files = os.listdir(root)

for file in files:
    # print(file)
    # 경로 + 파일명

    path = os.path.join(root, file)
    # print(path)
    if searchNm in files:
        check = input('이걸 찾나? '+ path + '? (y/n)')
        if check == 'y':
            break
        else:
            print('없음')