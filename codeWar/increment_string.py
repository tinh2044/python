def increment_string(s) :
    st = ''
    string =''
    for i in s:
        if ord(i) > 47 and ord(i) < 58:
            st += i
        else: string += i
    if len(st) >1 and int(st[len(st) - 1]) <= 9 and int(st) <= 9:
       return string + st[0:len(st) - 1] + str(int(st[len(st) - 1]) +1)
    elif st == '':
        st = '1'
        return string + st
    else: return string + str(int(st)+1)
    
print(increment_string('foobar99'))