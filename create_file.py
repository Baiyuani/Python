#!/usr/local/bin/python3
'''创建文件并写入内容

交互式
'''

import os

#获取文件名
def get_filename():

    while 1:
        fname = input('请输入文件名： ')
        if not os.path.exists(fname):
            break
        print('文件已存在')
    return fname

#获取文件内容
def get_content():

    cont = []
    print('请输入文件内容：')
    while 1:
        line =(input('(end to quit)'))
        if line == 'end':
            break
        cont.append(line + '\n')
    return cont

#写入文件
def write_file(fname,cont):
    with open(fname, 'w') as fn:
        fn.writelines(cont)

#代码主体

if __name__ == '__main__':
    fname = get_filename()
    cont = get_content()
    write_file(fname,cont)
