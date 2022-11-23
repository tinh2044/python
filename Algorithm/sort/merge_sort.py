def merge_sort(arr):
    new_arr = []
    if len(arr) <= 1:
        return arr
    left_arr = merge_sort(arr[:len(arr)//2])
    right_arr = merge_sort(arr[len(arr)//2:])
    
    while left_arr !=[] and right_arr !=[] :
        if (left_arr[0] > right_arr[0]):
            new_arr.append(right_arr[0])
            right_arr = right_arr[1:]
        else: 
            new_arr.append(left_arr[0])
            left_arr = left_arr[1:]
    if left_arr != []: new_arr.extend(left_arr)
    if right_arr != []: new_arr.extend(right_arr)
    return new_arr

print(merge_sort([5,7,3,1,8,4,0]))