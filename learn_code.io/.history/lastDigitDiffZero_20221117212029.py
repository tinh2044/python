def lastDigitDiffZero(n):
    a = 1;
    for i in range (1,n + 1):
        a *= i
    string = str(a)
    if (string.find('0')):
        
        return int(string[string.find('0') - 1])
    else :return int(string[len(string) - 1])
print(lastDigitDiffZero(10))