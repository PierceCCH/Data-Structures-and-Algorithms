def quickSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    lesser = []
    greater = []
    for i in arr:
        if i<pivot:
            lesser.append(i)
        else:
            greater.append(i)
    
    return quickSort(lesser) + [pivot] + quickSort(greater)

print(quickSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))