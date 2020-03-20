i = 1
while i < 10:
    j = 1
    while j <= i:
        print('%s * %s = %s' % (j, i, (i * j)), end=' ')
        j += 1
    i += 1
    print()