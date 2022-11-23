def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i
        for j in range(i-1, -1, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]
                index = j
            else: 
                break
        arr[index] = key
    return arr

print(insertion_sort([7,6,5,12,23,4,34,3,2,1]))