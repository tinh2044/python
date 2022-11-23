def lastDigitDiffZero(n):
    a = 1;
    for i in range (1,n + 1):
        a *= i
    l = str(a).split('').reverse()
    
    return [x for x in l if x > 0][0]
    
        
print(lastDigitDiffZero(20))