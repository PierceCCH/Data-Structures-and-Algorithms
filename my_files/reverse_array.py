def reverse_arr(str):
    arr = [e for e in str]
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - i-1]
        arr[len(arr)-i-1] = temp
    return ''.join(arr)

print(reverse_arr('0mjbnobnon '))
