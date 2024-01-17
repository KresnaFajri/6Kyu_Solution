def find_deleted_number(arr,mixed_arr):
    import collections
    None == 0
    if (collections.Counter(arr) == collections.Counter(mixed_arr)):
        return 0
    else:
        for x in arr :
            if x not in mixed_arr:
                return x
    
print(find_deleted_number([1,2,3,4,5],[3,4,1,5]))
print(find_deleted_number([1,2,3,4,5,6,7,8,9],[1,9,7,4,6,2,3,8]))
print(find_deleted_number([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]))