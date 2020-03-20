list = [0, 1]
l = int(input('输入长度： '))
for i in range(l - 2):
    list.append(list[-1] + list[-2])
print(list)