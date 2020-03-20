'''三位数，每一位的三次方之和等于这个数本身'''

for i in range(100,1000):
    num = str(i)
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
