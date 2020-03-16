'''创建用户'''

from subprocess import run
from sys import argv
from random import choice
from string import digits,ascii_letters

all_str = digits + ascii_letters + '_'

#获取8位的随机密码
def randpass(num = 8):
    _pass = ''
    for i in range(num):
        _pass += choice(all_str)
    return _pass

#创建用户，用户已存在时，返回提示信息，并退出脚本
def create_user():
    result = run('id %s &> /dev/null' % argv[1], shell=True)
    if result.returncode == 0:
        print('用户已存在！')
        exit()
    run('useradd %s' % argv[1], shell=True)

#为新用户设置8位的随机密码
def set_passwd():
    passwd = randpass()
    run('echo %s | passwd --stdin %s &> /dev/null' % (passwd, argv[1]), shell=True)
    return passwd

#将用户信息保存到指定文件中
def pass_file(passwd):
    content = ['username: %s\n' % argv[1], 'password: %s\n' % passwd]
    with open('%s' % argv[2], 'a') as fn:
        fn.writelines(content)

if __name__ == '__main__':
    create_user()
    passwd = set_passwd()
    pass_file(passwd)
    print('用户已创建，信息保存文件：%s' % argv[2])
