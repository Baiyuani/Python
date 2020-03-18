'''模拟用户登录'''

from getpass import getpass as p
import pickle
import os

def init():
    if not os.path.exists('pass.txt'):
        ulist = {'admin': 'password'}
        with open('pass.txt', 'wb') as fn:
            pickle.dump(ulist, fn)

def logup():
    username = input('请输入用户名： ').strip()
    if username == '':
        print('用户名不能为空！')
    elif username in _list:
        print('用户已存在')
    else:
        password = input('请输入密码： ')
        _list[username] = password

def login():
    username = input('请输入用户名： ')
    password = p('请输入密码： ')
    # password = input('mima: ')
    if _list[username] == password:
        print('登录成功!')
    else:
        print('用户名或密码错误！')

def menu():
    while 1:
        opt = input('''（0）注册
（1）登录
（2）退出
请输入：''')
        cmds = {'0': logup, '1': login}
        if opt not in ['0', '1', '2']:
            print('输入错误！')
            continue
        if opt == '2':
            with open('pass.txt', 'wb') as fn:
                pickle.dump(_list, fn)
            print('bye')
            break
        cmds[opt]()

if __name__ == '__main__':
    init()
    with open('pass.txt', 'rb') as fn:
        _list = pickle.load(fn)
    menu()
