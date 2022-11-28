def numberZeroDigits(n):
    tong = 1
    for i in range(1,n+1):\
        tong *= i
    count = 0
    string = str(tong)
    for i in string[::-1]:
        if (i == "0"):
            count += 1
        else: break
print(numberZeroDigits(100))