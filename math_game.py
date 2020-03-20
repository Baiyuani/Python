import random

def exam():
    nums = [random.randint(1,100) for i in range(2)] #取两个随机数
    nums.sort(reverse=True)  #排序
    opt = random.choice('+-×÷')  #抽取选项
    #函数字典
    dic = {'+': lambda x, y:x + y, '-': lambda x, y:x - y, '×': lambda x, y:x * y, '÷': lambda x, y:x // y}
    #保存正确结果
    result = dic[opt](*nums)
    #提示内容
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
        try:
            #取出用户输入的两端空格，然后取出首字母
            opt = input('继续吗？（y/n）').strip()[0]
        except:
            opt = 'y'
        if opt in 'Nn':
            print('\nbye-bye')
            break

if __name__ == '__main__':
    menu()