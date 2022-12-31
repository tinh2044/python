def isTandemRepeat(inputString):
    n = len(inputString) /2
    i = 0
    j = 2
    if (ord(inputString[0]) > 47 and ord(inputString[0]) < 59) :
        j = 1
    string = ""
    check = False
    while j <= n:
        
        string = inputString[0:j]
        z = j
        new_str =""
        check_2 = True
        while z <= (n*2)-j and check_2:
            if(string == inputString[z:z+j]):
                z += j
            else:
                check_2 = False
                
        if (z == (n*2)) : 
            check = True
            break
        j += 1
    if (check): return True 
    else: return False
print(isTandemRepeat("qqq"))
# print(ord("9"))