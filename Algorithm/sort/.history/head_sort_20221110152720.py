def heapify(arr , n , index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2
    
    if (left < n and arr[left] > arr[largest]):
        largest = left
    if (right < n and arr[right] > arr[largest]):
        largest = right
    if (largest != index):
        arr[largest], arr[index] =  arr[index], arr[largest]	
        heapify(arr, n , largest)
        
arr = [2, 4, 5, 12, 6, 7, 8]
def heap_sort(arr):
    index = (len(arr) // 2) -1
    for i in range(index, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1,-1, -1):
        print(le(arr))
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i)
    return arr
print(heap_sort(arr))