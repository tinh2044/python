def bin(arr):
    print(arr)
    i = len(arr) - 1
    while (arr[0] == 1):
        i -= 1
    if (i == 0):
        return 
    else: 
        arr[i] = 1
        j = i +1
        while (j < len(arr)):
            arr[j] = 0
        
    
    
    
bin([0, 0, 0 ,0])