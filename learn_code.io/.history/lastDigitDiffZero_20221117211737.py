def lastDigitDiffZero(n):
    a = 1;
    for i in range (1,n + 1):
        a *= i
    string = str(a)
    return string[string.find('0') - 1]

print(lastDigitDiffZero(6))