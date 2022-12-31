def truncateString(s):
    l = [int(x) for x in s]
    i = 0 
    while (i < len(l)):
        if (l[i]%3 ==0) : 
            l = l[i+1:]
            i = 0
        elif (l[i] + l[len(l)-i-1])%3 ==0:
            i = 0
            l = l[i+1:len(l)-i-1]
        elif l[len(l) - 1]%3 == 0:
            l = l[:len(l)-1]
        else: i += 1
    return "".join([str(i) for i in l])
print(truncateString("57439552816"))