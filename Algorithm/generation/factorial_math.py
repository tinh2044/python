def factorialMath(arr):
    print(arr)
    n = len(arr)
    i = n - 2
    while (i >= 0 and arr[i] > arr[i + 1]):
        i -=1
    if (i == -1) :return
    elif (i == n -2): arr[i],arr[i + 1] = arr[i + 1],arr[i]
    else:
        z = n -1
        while arr[i] > arr[z]:
            z -= 1
        arr[i], arr[z] = arr[z], arr[i]
        l = i+1
        r = n -1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return factorialMath(arr)
    
factorialMath([1,2,3,4])