import random

def exam():
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    opt = random.choice('+-×÷')
    dic = {'+': lambda x, y:x + y, '-': lambda x, y:x - y, '×': lambda x, y:x * y, '÷': lambda x, y:x // y}
    result = dic[opt](*nums)
    prompt = '%s %s %s = ' % (nums[0], opt, nums[1])
    count = 0
    while count < 3:
        try:
            answer = int(input(prompt))
        except:
            count +=1
            continue

        if answer == result:
            print('答对了！')
            break
        print('不对')
        count += 1
    else:
        print('正确答案：%s%s' % (prompt, result))

def menu():
    while 1:
        exam()
        opt = input('继续吗？（y/n）')
        if opt in 'Nn' and opt != '':
            print('\nbye-bye')
            break

if __name__ == '__main__':
    menu()