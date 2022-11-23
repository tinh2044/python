n = 24

def factorSum(n):
    sum = 0
    i = 2
    while (n >= i):
        while (n % i == 0):
            sum += i
            n //= i
        i += 1
    check = isPrime(sum)

    if (check): return sum
    else: return factorSum(sum)

    # return sum

def isPrime(n):
    if (n == 0) : return False
    check = True
    i = 2
    while (check and i < n):
        if (n % i == 0) :
            check = False
        i += 1
    return check

print(factorSum(n))