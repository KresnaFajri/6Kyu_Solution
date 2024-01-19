def find_it(seq):
    i = 0
    lst_count = []
    for element in seq:
        seq.count(seq[i])
        if seq.count(seq[i]) % 2 != 0:
            return seq[i]
        i += 1
    return seq[i]
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))