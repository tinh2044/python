def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1,len(arr), 1):
            if (arr[j] < arr[min]):
                min = j
        arr[i],arr[min] = arr[min], arr[i]
    return arr

print(selection_sort([5,7,4,3,1,6]))
        