def quick_sort(arr, left, right):
    if left < right:
        # pivot = partition(arr, left, right)
        pivot = hoare(arr, left, right)
        quick_sort(arr,left, pivot -1)
        quick_sort(arr,pivot +1, right)
    
def partition(arr, left, right):
    pivot = arr[right]
    i = left -1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            
    if arr[i+1] > arr[right]:
        arr[right], arr[i+1] = arr[i+1],arr[right]
    return i+1

def hoare (arr, left, right):
    pivot = arr[right]
    while True:
        while arr[left] < pivot and left < right:
            left += 1
        while arr[right] > pivot and left < right:
            right -= 1
        # if left < right: 
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        if left >= right:
            return left
        # if arr[right] == arr[left] : left += 1
        
        

a =[1,5,4,2,4,6,2,1]
quick_sort(a, 0 ,len(a) -1 )
print(a)