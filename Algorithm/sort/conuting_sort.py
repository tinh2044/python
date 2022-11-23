from functools import reduce

def counting_sort(arr):
    m = max(arr)
    list_1 = [x-x for x in range(m+1)]
    new_arr = []
    for i in arr:
        list_1[i] += 1
    for i in range(len(list_1)):
        if list_1[i] != 0 :
            for j in range(list_1[i]):
                new_arr.append(i)
    return new_arr
    
print(counting_sort([4,4,4,3,3,3,2,2,1,7,6,8,6]))