def dig_pow(n,p):
    list_num = list(map(int,(str(n))))
    i = 0
    p = p
    for numbers in list_num:
        list_num[i] = (list_num[i]**(p))
        i += 1
        p += 1
    if sum(list_num) % n == 0:
        return( sum(list_num) // n)
    elif sum(list_num) % n != 0:
        return -1
print(dig_pow(46288,3))

