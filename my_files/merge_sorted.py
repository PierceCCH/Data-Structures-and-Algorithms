def mergeSort(arrA, arrB):
    if len(arrA) == 0 or len(arrB) == 0:
        return arrA + arrB
    ls = []
    i = 0
    j = 0
    while i<len(arrA) and j<len(arrB):
        if arrA[i] <= arrB[j]:
            ls.append(arrA[i])
            i += 1
        
        elif arrA[i] >= arrB[j]:
            ls.append(arrB[j])
            j += 1
    
    return ls + arrA[i:] + arrB[j:]



print(mergeSort([], [2,4,6]))