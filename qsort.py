from random import randint

def qsort(seq):
    '接受一个序列对象，返回排序结果'
    if len(seq) < 2:
        return seq

    # 假设第1项是中间值
    middle = seq[0]
    smaller = []
    larger = []
    # 遍历后续项，比middle小的放到samller，比middle大的放到larger
    for data in seq[1:]:
        if data < middle:
            smaller.append(data)
        else:
            larger.append(data)

    # 把3项数据拼接
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = qsort(nums)
    print(result)
