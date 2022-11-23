def greatestCommonPrimeDivisor(a,b):
    c = 0
    l = []
    
    if (a > b):
        c = b
    else: c = a
    
    for i in range(2), c+1):
        if ( a % i == 0 and b % i == 0):
            l.append(i)
    l = sorted(l, reverse=True)
    l.append(-1)
    l_1 = [x for x in l if (isPrime(x))]
    return l_1[0]
def isPrime(n):
    if n <=1 and n < -1 : return True
    elif n < 0 : False
    i = 2
    while (i < n):
        if (n % i ==0) : return False
        i += 1
    return True
print(greatestCommonPrimeDivisor(12, 13))