def recurring(arr):
    hash_table = {}
    for i in arr:
        if i not in hash_table.keys():
            hash_table[i] = i
        else:
            return i
    return "No recurring"

print(recurring([1,2,2,1, 2,3,4,5,5,6,7,8]))