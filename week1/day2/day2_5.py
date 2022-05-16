import os
# 재귀함수 호출
def fn_print_files(root):
    files = os.listdir(root)
    for file in files:
        path = os.path.join(root,file)
        print(path)
        if os.path.isdir(path):
            fn_print_files(path)
fn_print_files('/home/pc52/Public')
def fn_print_files2(root, param):
    files = os.listdir(root)
    for file in files:
        path = os.path.join(root, file)
        print(path)
        if param in file:
            msg = input(path + '이거?(y/n)')
        if os.path.isdir(path):
            fn_print_files2(path, param)
fn_print_files2('/home/pc43/Downloads', 'member')