def numberZeroDigits(n):
    tong = 1
    for i in range(1,n+1):\
        tong *= i
    string  = str(tong)
    if string.includes("0"):
        return len(string[string.index("0"):])
    else: return 0
print(numberZeroDigits(5))