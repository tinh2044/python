def combinatorics(arr, k, n):
    print(arr)
    i = len(arr)
    while (i >= 1 and arr[i - 1] == n - k + i):
        i -= 1
    if (i == 0): return
    elif (i == len(arr)) : arr[i - 1] += 1
    else: 
        arr[i - 1] += 1
        for j in range(i,len(arr)):
            arr[j] = arr[j-1] + 1
    return combinatorics(arr, k , n)

combinatorics([1, 2],2 ,4 )
    
# 1 2
# 1 3 
# 1 4  
# 2 3
# 2 4
# 3 4