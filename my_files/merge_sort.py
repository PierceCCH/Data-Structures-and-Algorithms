def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print("Left: {} Right: {}".format(left, right))

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    l = 0
    r = 0
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    print("Left_M: {} Right_M: {}".format(left, right))
    return res + left[l:] + right[r:]

print(mergeSort([99,44,6,2,1,5,63,87,283,4,0]))