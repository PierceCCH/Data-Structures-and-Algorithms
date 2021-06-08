def selectionSort(arr):
    for i in range(len(arr)):
        index = i
        smallest = arr[index]
        for j in range(i, len(arr)):
            if arr[j] < smallest:
                index = j
                smallest = arr[j]
        temp = arr[i]
        arr[i] = smallest
        arr[index] = temp
    
    return arr

print(selectionSort([31,24,3125,123,4,6,2,4,6,0,5,43,1,5,4,6,2,12]))

