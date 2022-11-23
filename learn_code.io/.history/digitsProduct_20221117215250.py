def digitsProduct(n):
    if isPrime(n) : return -1
    
    l = []
    i = 2
    while n >= 1:
        while n % i == 0:
            l.append(i)
            n //= i
    return int(''.join(l))
print(digitsProduct(450))