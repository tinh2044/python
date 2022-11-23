def bin(arr):
    print(arr)
    i = len(arr) - 1
    while (arr[0] == 1):
        i -= 1
    if (i == 0):
        return 
    else: arr[i] = 1
    
    
    
bin([0, 0, 0 ,0])