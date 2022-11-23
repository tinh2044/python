a = [1,3,4,5,9,4,6,8,10,4]

def merge_sort(arr):
    if (len(arr) <= 1) :
        return arr
    else:
        left = arr[:len(arr) // 2]    
        right = arr[len(arr) // 2:]    
        left_arr = merge_sort(left)
        right_arr = merge_sort(right)
        return s(left_arr, right_arr)
    
    


def s(a, b):
    c = []
    while a != [] and b != []:
        if a[0] < b[0]:
            c.append(a[0])
            a = a[1:]
        else: 
            c.append(b[0])
            b = b[1:]
    if a != []: c += a
    if b != []: c += b
    return c
print(merge_sort(a))