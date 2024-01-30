def digital_root(n):
    import numpy as np
    list_n = []
    list_n.append(n)

    #creating list of integer to be summed
    list_int = list(map(int,str(list_n[0])))
    output = np.sum(list_int)
    #creating converted output list (integer) to string, in order to search the length of number
    CONV_OUTPUT = list(str(output))
    if len(CONV_OUTPUT) > 1:
        while len(CONV_OUTPUT) > 1:
            output = np.sum([eval (x) for x in CONV_OUTPUT])
            CONV_OUTPUT = CONV_OUTPUT = list(str(output))
    return output
print(digital_root(16))
print(digital_root(493193))