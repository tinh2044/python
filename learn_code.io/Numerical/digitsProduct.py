
def digitsProduct(n):
    if isPrime(n) : return -1
    if n ==0 : return 0
    
    l = []
    # i = 2
    while n >1:
        i = 9
        while (i > 1):
           if (n % i == 0): 
               l.append(i)
               n //= i   
               break
           i -= 1
    l.reverse()
    # print("".join([str(x) for x in l]))
    s = ""
    for i in l :
        s += str(i)
    return int(s)



def isPrime(n):
    if n <=1 and n < -1 : return True
    elif n < 0 : False
    i = 2
    while (i < n):
        if (n % i ==0) : return False
        i += 1
    return True
print(digitsProduct(450))