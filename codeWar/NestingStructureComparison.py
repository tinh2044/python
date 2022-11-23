def same_structure_as(original, other):
    if len(l) != len(m):
        return False
    else:
        for i in range(len(original)):
            if type(original[i]) != type(other[i]):
                return False
            elif type(original[i]) == 'list':
                pass


l = [1, 1, 1]
m = [2, 2, 2]
print(same_structure_as(l, m))
print(type(m) == "list")
