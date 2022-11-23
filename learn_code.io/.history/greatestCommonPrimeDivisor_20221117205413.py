def greatestCommonPrimeDivisor(a,b):
    c = 0
    l = []
    
    if (a > b):
        c = b
    else: c = a
    
    for i in range(1, c+1):
        if ( a % i == 0 and b % i == 0):
            l.append(i)
    l = sort(l)
    return l

print(greatestCommonPrimeDivisor(12, 18))