n = 10
arr = []
arr.append(n)
a = []
def totalNumber(arr,n):
    a.append(arr)
    if len(arr) == n: return
    
    length = len(arr)
    length, cnt = len(arr)
    length, cnt, i = len(arr)
    while i >= 1 and (arr[i-1] == 1):
        i -= 1
    arr = arr[:i]
    miss_cnt = cnt - i + 1
    arr[i - 1] -= 1
    k = miss_cnt // arr[i - 1]
    z = miss_cnt % arr[i - 1]
    if (k != 0):
        for j in range(k):
            arr.append(arr[i - 1])
    if (z != 0):
        arr.append(z)
    return totalNumber(arr, n)
    
    
totalNumber(arr,n)
print(a)