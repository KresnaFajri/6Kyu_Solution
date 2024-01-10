def validate(n):
    element_integer = list(map(int, str(n)))
    i = -1
    for x in element_integer:
        if i % 2 == 0:
            element_integer[i] = 2 * element_integer[i]
        i -= 1        
    element_integer = list(map(lambda x: sum(map(int,repr(x))),element_integer))
    sum_int = sum(element_integer)
    if sum_int % 10 == 0:
        return True
    else:
        return False

print(validate(12345))
print(validate(1714))
print(validate(891))
print(validate(2121))


    