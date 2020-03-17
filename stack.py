'''栈结构模拟'''

contents = []

def _put():
    data = input('(data:) ').strip()
    contents.append(data) if data else print('\033[31;1m请输入内容\033[0m')

def _get():
    print('\033[32;1m%s\033[0m' % contents.pop()) if contents else print('\033[31;1mEmpty stack!\033[0m')

def _dis():
    print('\033[32;1m%s\033[0m' % contents) if contents else print('\033[31;1mEmpty stack!\033[0m')

if __name__ == '__main__':
    cmds = {'0': _put, '1': _get, '2': _dis}
    while 1:
        print('''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出''')
        opt = input('请选择(0/1/2/3): ')
        if opt not in ['0', '1', '2', '3']:
            print('\033[31;1m输入错误！\033[0m')
            continue
        if opt == '3':
            print('\033[31;1mbye\033[0m')
            break
        cmds[opt]()
