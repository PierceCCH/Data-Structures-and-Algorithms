def fibbonaci(n):

    #base cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    #recursive case
    return fibbonaci(n-1) + fibbonaci(n-2)

print(fibbonaci(5))