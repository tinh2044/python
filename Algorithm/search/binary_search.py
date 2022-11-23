def binary_search(arr,x):
    left = 0
    right = len(arr) -1
    mid = (left + right) // 2
    while True :
        if x == arr[mid] or x == arr[left] or x == arr[right]:
            print(arr.index(x))
            break
        elif x > arr[mid]: left = mid + 1
        elif x < arr[mid]: right = mid - 1
        elif left > right: break
            
    
binary_search([1,2,3,4,5,6,7,8,9], 4)