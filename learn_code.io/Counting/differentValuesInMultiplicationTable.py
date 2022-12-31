def differentValuesInMultiplicationTable2(n,m):
    l = [ [(x+1) * (y+1) for y in range(m)]  for x in range(n) ]
    new_l = []
    for i in l:
        for j in i:
            new_l.append(j)
    
    return len(set(new_l))
print(differentValuesInMultiplicationTable2(3,2))