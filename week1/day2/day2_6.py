import os
path = '/home/pc52/Downloads'
#디폴트 top-down : 상위 -> 하위로
#topdown=False : 하위에서 -> 상위로
# for root, dirs, files in os.walk(path):
for root, dirs, files in os.walk(path, topdown=False):
    print(root,dirs,files)