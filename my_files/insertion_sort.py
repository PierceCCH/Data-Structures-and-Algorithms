def insertionSort(arr):
    for i in range(len(arr)):
        current = arr[i]
        while i>0 and arr[i-1]>current:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr

print(insertionSort([12,345,6, 1,1, 2, 5,3,123,45,1234,34,23]))

            