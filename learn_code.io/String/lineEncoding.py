def lineEncoding(s):
    new_s = ""
    s = s + " "
    i = 0
    while i < len(s) -1:
        count = 1
        while i < len(s) and s[i] == s[i+1]:
            i += 1
            count = count + 1
        if (count == 1) :
            new_s = new_s + s[i]
        else :
            new_s = new_s + str(count) + s[i]
        count = 1
        i += 1
    return new_s
print(lineEncoding("aaadddaaaeeea"))