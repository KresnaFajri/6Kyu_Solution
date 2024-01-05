def persistence(n):
    import numpy as np
    list_int = list(map(int,str(n)))
    result = 1
    count = 0
    if len(list_int) == 1:
        return count
    else:
        while len(list_int) > 1:
            result = np.prod(list_int)
            list_int = list(map(int,str(result)))
            count += 1
    return count

print(persistence(4))
print(persistence(39))
print(persistence(25))
print(persistence(999))
