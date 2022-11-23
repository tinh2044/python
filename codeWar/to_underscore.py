def to_underscore(s) :
    for i in s:
        if ord(i) >64 and ord(i) < 91:
            s  = s.replace(i, '_'+i.lower())
    return s
print(to_underscore('nguyenChiTinh'))