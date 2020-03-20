from time import strftime
import os
import pickle

def save(fname):
    '用于记录收入'
    jine = int(input('金额：'))
    beizhu = input('备注： ')
    date = strftime('%Y-%m-%d')
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    yue = records[-1][-2] + jine
    record = [date, jine, 0, yue, beizhu]
    records.append(record)
    # 把收支情况写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    '用于记录支出'
    jine = int(input('金额：'))
    beizhu = input('备注： ')
    date = strftime('%Y-%m-%d')
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    yue = records[-1][-2] - jine
    record = [date, 0, jine, yue, beizhu]
    records.append(record)
    # 把收支情况写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    '用于查询收支情况'
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for line in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))

def show_menu():
    '显示菜单'
    # 项目初始化
    fname = 'account.data'
    if not os.path.exists(fname):
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    funcs = {'0': save, '1': cost, '2': query}

    tishi = '''(0) 收入
(1) 支出
(2) 查账
(3) 退出
请选择(0/1/2/3): '''
    while 1:
        xuanze = input(tishi).strip()
        if xuanze not in ['0', '1', '2', '3']:
            print('无效的输入，请重试')
            continue

        if xuanze == '3':
            print('\nBye-bye')
            break

        funcs[xuanze](fname)

if __name__ == '__main__':
    show_menu()

