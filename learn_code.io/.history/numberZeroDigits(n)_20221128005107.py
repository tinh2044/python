def numberZeroDigits(n):
    tong = 1
    for i in range(1,n+1):\
        tong *= i
    return tong
    string  = str(tong)
    if string.find("0") > 0:
        return len(string[string.index("0"):])
    else: return 0
print(numberZeroDigits(100))