def digitsProduct(n):
    if isPrime(n) : return -1
    
    l = []
    # i = 2
    while n >1:
        i = 9
        while (i > 1):
           if (n % i == 0): 
               l.append(i)
               n //= i   
           i -= 1
    return l



def isPrime(n):
    if n <=1 and n < -1 : return True
    elif n < 0 : False
    i = 2
    while (i < n):
        if (n % i ==0) : return False
        i += 1
    return True
print(digitsProduct(450))