'''模拟用户登录'''

import getpass

ulist = {}

def logup():
    username = input('请输入用户名： ').strip()
    if username == '':
        print('用户名不能为空！')
    elif username in ulist:
        print('用户已存在')
    else:
        password = input('请输入密码： ')
        ulist[username] = password

def login():
    username = input('请输入用户名： ')
    password = getpass.getpass('请输入密码： ')
    if ulist.get(username) == password:
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
            print('bye')
            break
        cmds[opt]()

if __name__ == '__main__':
    menu()
