def bin(arr):
    
    i = len(arr) - 1
    while (arr[0] == 1):
        i -= 1
    arr[i] = 1
    
bin([0, 0, 0 ,0])