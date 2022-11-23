def digitsProduct(n):
    if isPrime(n) : return -1
    
    x = 1
    y = 1
    check = x*y != n
    while (check ):
        y = 1
        while (y < 10 and check ):
            if (x*y == n) :
                check = True
            else:
                y += 1
        if (check ):
            x += 1
        
    return int(str(x) + str(x))
    
    
    
def isPrime(n):
    if n <=1 and n < -1 : return True
    elif n < 0 : False
    i = 2
    while (i < n):
        if (n % i ==0) : return False
        i += 1
    return True

print(digitsProduct(12))