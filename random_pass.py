from random import choice
from string import digits,ascii_letters

all_str = digits + ascii_letters + '_'

def randpass(num = 8):
    _pass = ''
    for i in range(num):
        _pass += choice(all_str)
    return _pass

if __name__ == '__main__':
    print(randpass(int(input('请输入要获取的密码长度： '))))
