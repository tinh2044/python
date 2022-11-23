def digitsProduct(n):
    if isPrime(n) == False : return -1
    
    x = 1
    y = 1
    while (x*y != n):
        y = 1
        while (y < 10 and x*y != n):
            y += 1
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

print(digitsProduct(24))