def disemvowel(string_):
    disemvowel_string = list(filter(lambda x:x not in ['a','i','u','e','o','A','I','U','E','O'],string_))
    result = "".join(disemvowel_string)
    return result

print(disemvowel('ElloH woRld'))
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))