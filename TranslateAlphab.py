#In this code, I try to convert alphabet to a number based on their index in integer. 
def translate(n):
    list_alpha = list(n)
    result = []
    alpha_dictio = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e': 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j': 10
                    ,'k' : 11, 'l' : 12, 'm':13, 'n': 14, 'o': 15, 'p':16, 'q':17, 'r':18, 's':19,'t':20, 'u':21,'v':22,'w':23,'x':24,'y':25, 'z':26}
    i = 0
    for x in list_alpha:
        result.append(alpha_dictio[list_alpha[i]])
        i += 1
    result = list(map(str,result))
    code_numbers = ''.join(result)
    return code_numbers

#Testing Project

print(translate('ahjkmop'))
