def bin(arr):
    print(''.join([str(x) for x in arr]))
    print()
    i = len(arr) - 1
    while (arr[i] == 1 and i >= 0):
        i -= 1
    if (i == -1):
        return 
    else:
        arr[i] = 1
        j = i +1
        while (j < len(arr)):
            arr[j] = 0
            j += 1
        bin(arr)
bin([0,0,0,0,0])