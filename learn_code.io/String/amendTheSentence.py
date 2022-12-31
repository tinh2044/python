def amendTheSentence(s):
    l = []
    j = 0
    for i in range(1,len(s)):
        if ord(s[i]) < 97:
            # print(s[i])
            l.append(s[j:i].lower())
            j = i
        if (i == len(s)-1):
            print(s[i])
            l.append(s[j:].lower())
    return " ".join(l)
    
print(amendTheSentence("vSKwWDjwIerQKMgVaAniorRJlerbKpDgvyKBLPNwSRWtylqKewNFtERNuUBBHAsGkTSSfdhQHJYvAighAdeG"))
# "v s kw w djw ier q k mg va anior r jlerb kp dgvy k b l p nw s r wtylq kew n ft e r nu u b b h as gk t s sfdh q h j yv aigh ade g"