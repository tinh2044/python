def primeSum(n):
    list_1 = []
    while n > 2:
        check = isPrime(n)
        if check:
            list_1.append(n)
        if (n % 2 != 0):
            n -= 2
        else: n -=1
    list_1.append(2) 
    return sum(list_1)
def isPrime(n):
    if (n == 0) : return False
    check = True
    i = 2
    while (check and i < n):
        if (n % i == 0) :
            check = False
        i += 1
    return check
print(primeSum(10000))