def differentSubstringsTrie(inputString):
    l = []
    len_s = len(inputString)
    for i in range(0, len_s, 1):
        for j in range( i+1,len_s+1, 1):
            l.append(inputString[i:j])
            
    return len(set(l))
print(differentSubstringsTrie("abacaba"))