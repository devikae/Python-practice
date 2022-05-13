import shutil
import os

from_ = 'bot.py'
to_ = './backup'

#특정 폴더를 백업시켜 이동시킬 수 있음.

if not os.path.exists(to_):
    #찾지 못했다면 폴더 생성
    os.makedirs(to_)
#파일이동
shutil.move(from_, to_)

